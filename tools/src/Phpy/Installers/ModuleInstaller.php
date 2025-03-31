<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Installers;

use Composer\Semver\Semver;
use PhpyTool\Phpy\Application;
use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\ConsoleIO;
use PhpyTool\Phpy\Exceptions\CommandFailedException;
use PhpyTool\Phpy\Exceptions\CommandStopException;
use PhpyTool\Phpy\Helpers\PackageCollector;
use PhpyTool\Phpy\Helpers\Process;
use PhpyTool\Phpy\Helpers\PythonMetadata;
use PhpyTool\Phpy\Helpers\System;
use PhpyTool\Phpy\Helpers\Version;
use RecursiveDirectoryIterator;
use RecursiveIteratorIterator;
use Symfony\Component\Console\Question\ConfirmationQuestion;

class ModuleInstaller implements InstallerInterface
{
    /**
     * @var Config
     */
    protected Config $config;

    /**
     * @var ConsoleIO|null
     */
    protected null|ConsoleIO $consoleIO;

    /**
     * @var Process
     */
    protected Process $process;


    public function __construct(Config $config, null|ConsoleIO $consoleIO = null)
    {
        $this->config = $config;
        $this->consoleIO = $consoleIO;
        $this->process = $consoleIO?->getExtra('process') ?: new Process($consoleIO);
    }

    /**
     * @return void
     */
    public function scan(): void
    {
        $this->consoleIO?->output('Scanning for modules ...');
        $dirs = $this->config->get('config.scan-dirs');
        if (!$dirs) {
            throw new CommandStopException('Nothing to scan');
        }
        $packages = [];
        $cwd = System::getcwd();
        foreach ($dirs as $dir) {
            $dir = !str_starts_with($dir, '/') ? "$cwd/$dir" : ($cwd . $dir);
            if (!is_dir($dir)) {
                $this->consoleIO?->comment("Skip $dir");
                continue;
            }
            $files = $this->findPhpFiles(realpath($dir));
            foreach ($files as $file) {
                $this->consoleIO?->output("Scanning <info>$file</info>");
                $scannedPackages = PackageCollector::parseFile($file);
                foreach ($scannedPackages as $package) {
                    $this->consoleIO?->subOutput("<comment>--</comment> scanned: <comment>$package</comment>");
                }
                $packages = array_merge($packages, $scannedPackages);
            }
        }
        $packages = array_unique($packages);
        $pushing = [];
        $modules = [];
        foreach ($packages as $package) {
            $package = explode('.', $package)[0];
            if (PythonMetadata::isStdLibrary($package)) {
                continue;
            }
            if (!$moduleName = PythonMetadata::getPipPackage($package)) {
                $moduleName = $this->consoleIO?->ask(
                    "No module information found for top_level <info>$package</info>. Please enter the module name for top_level <info>$package</info>:",
                    ''
                );
                if (!$moduleName) {
                    $this->consoleIO?->comment("<comment>--</comment> skipped: <comment>$package</comment>");
                    continue;
                }
                $pushing[] = [
                    'module_name' => $moduleName,
                    'top_level' => $package,
                    'version' => 'default',
                ];
            }

            if ($availableVersions = Version::getPepVersions($moduleName)) {
                foreach ($availableVersions as $key => &$availableVersion) {
                    if (!$availableVersion = Version::pepToSemver($availableVersion)) {
                        unset($availableVersions[$key]);
                    }
                }
                $vMap = Version::splitVersion(Semver::rsort($availableVersions)[0]);
                $modules[$moduleName] = "^$vMap[0].$vMap[1]";
            }
        }
        if ($modules) {
            $count = count($modules);
            $this->consoleIO?->output("Scanned: $count");
            foreach ($modules as $module => $version) {
                $this->consoleIO?->subOutput("<comment>--</comment> <info>$module</info> - <comment>$version</comment>");
            }
        }
        if (!$this->consoleIO?->ask(
            "Do you want to install these modules? [<comment>Y,n</comment>]",
            true,
            questionClass: ConfirmationQuestion::class
        )) {
            throw new CommandStopException('PHPy will not install any modules');
        }
        // 保存到配置 local
        $this->config->set('modules', array_merge($this->config->get('modules', []), $modules));

        // 写入文件
        System::putFileContent(System::getcwd() . '/phpy.json', (string)$this->config);
        // 推送
        try {
            if ($pushing) {
                foreach ($pushing as $item) {
                    PythonMetadata::pushMetadata($item['top_level'], $item['module_name'], $item['version']);
                }
            }
        } catch (\Throwable) {}
    }

    /** @inheritdoc */
    public function install(): void
    {
        $phpyHash = $this->config->get('phpy-hash');
        $composerHash = $this->config->get('composer-hash');
        // 如果存在 phpy-hash 和 composer-hash， 则为install
        if ($phpyHash and $composerHash) {
            $this->consoleIO?->output('Installing modules ...');
            $installModules = $this->config->get('install-modules', []);
        } else { // 不存在，则为update
            $this->consoleIO?->output('Updating modules ...');
            // 获取local
            $locals = $this->config->get('modules', []);
            // 获取vendor
            $vendors = [];
            Application::getVendorConfigFiles(function ($organization, $package, $configFilePath) use (&$vendors) {
                $config = new Config($configFilePath);
                $modules = $config->get('modules', []);
                foreach ($modules as $module => $versionConstraint) {
                    $vendors[$module][$versionConstraint] = [
                        'organization' => $organization,
                        'package' => $package,
                    ];
                }
            });
            $this->config->set('vendors', $vendors);
            $verMapCache = [];
            // 检查locals
            $localModules = [];
            foreach ($locals as $module => $versionConstraint) {
                // 版本映射储存
                $verMapCache[$module] = $availableVersions = $this->availableVersions($module);
                $localModules[$module] = $this->satisfyingVersions($module, array_keys($availableVersions), $versionConstraint);
            }
            // 检查vendors
            $vendorModules = [];
            foreach ($vendors as $module => $item) {
                // 如果本地存在的module则不需要拉取远端可用版本列表，否则则拉取
                if ($local = isset($localModules[$module])) {
                    $availableSemverVersions = $localModules[$module];
                } else {
                    $verMapCache[$module] = $availableVersions = $this->availableVersions($module);
                    $availableSemverVersions = array_keys($availableVersions);
                }
                // 循环检查所有组织/包的版本约束
                foreach ($item as $versionConstraint => $info) {
                    $availableSemverVersions = $this->satisfyingVersions($module, $availableSemverVersions, $versionConstraint, $info);
                }
                if (!$local) {
                    $vendorModules[$module] = $availableSemverVersions;
                } else {
                    $localModules[$module] = $availableSemverVersions;
                }
            }
            // semver -> pep 440
            foreach ($localModules as $module => $semverVersions) {
                // 取出最新版本，获取PEP440映射
                $localModules[$module] = $verMapCache[$module][$semverVersions[0]];
            }
            foreach ($vendorModules as $module => $semverVersions) {
                // 取出最新版本，获取PEP440映射
                $vendorModules[$module] = $verMapCache[$module][$semverVersions[0]];
            }
            $installModules = array_merge($localModules, $vendorModules);
            // 写入安装的模块
            $this->config->set('install-modules', $installModules);
            // 写入hash
            $this->config->set('phpy-hash', hash_file('SHA256', System::getcwd() . '/phpy.json'));
            // 写入composer-hash
            $this->config->set('composer-hash', hash_file('SHA256', System::getcwd() . '/composer.json'));
        }

        if ($installModules) {
            $this->pipModulesInstall($installModules);
        } else {
            $this->consoleIO->output('No modules need to install.');
        }
    }

    /** @inheritdoc */
    public function uninstall(): void
    {
    }

    /** @inheritdoc */
    public function upgrade(): void
    {
        if ($hash = $this->config->get('phpy-hash')) {
            $phpyHash = hash_file('SHA256', System::getcwd() . '/phpy.json');
            if ($phpyHash !== $hash) {
                $this->config->set('phpy-hash', null);
            }
        }
        if ($hash = $this->config->get('composer-hash')) {
            $composerHash = hash_file('SHA256', System::getcwd() . '/composer.json');
            if ($composerHash !== $hash) {
                $this->config->set('composer-hash', null);
            }
        }
        $this->install();
    }

    /** @inheritdoc */
    public function clearCache(): void
    {
    }


    /**
     * 查找php文件
     *
     * @param $directory
     * @return array
     */
    private function findPhpFiles($directory): array
    {
        $phpFiles = [];
        $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory));
        foreach ($iterator as $file) {
            if ($file->isFile() && pathinfo($file->getFilename(), PATHINFO_EXTENSION) === 'php') {
                $phpFiles[] = $file->getPathname();
            }
        }
        return $phpFiles;
    }

    /**
     * 获取可用的Python模块版本
     *
     * @param string $module
     * @param array $availableSemverVersions
     * @param string $versionConstraint
     * @param array<string, string> $info
     * @return array
     */
    private function satisfyingVersions(string $module, array $availableSemverVersions, string $versionConstraint, array $info = []): array
    {
        $organization = $info['organization'] ?? null;
        $package = $info['package'] ?? null;
        $msg = ($organization and $package)
            ? "Package <info>{$info['organization']}/{$info['package']}</info>"
            : "Local";
        // 检查版本是否满足约束
        $satisfyingVersions = Semver::satisfiedBy($availableSemverVersions, $versionConstraint);
        if (!$satisfyingVersions) {
            $this->consoleIO?->output(<<<EOT
$msg
Python module <info>$module</info>-<comment>$versionConstraint</comment>> not found in pip.

Read more about <comment>https://pypi.org/search</comment>
EOT
            );
            throw new CommandFailedException('Failed.');
        }
        // 选择满足约束的版本列表
        return Semver::rsort($satisfyingVersions);
    }

    /**
     * 返回pip可用版本列表
     *
     * @param string $module
     * @return array<string, string> = [semverVersion => pepVersion]
     */
    public function availableVersions(string $module): array
    {
        // 查询 pip 库中的模块版本
        if (!$moduleVersions = Version::getPepVersions($module)) {
            $this->consoleIO?->output(<<<EOT
Python module <comment>$module</comment> not found in pip.

Read more about <comment>https://pypi.org/search</comment>
EOT
            );
            throw new CommandFailedException('Failed.');
        }
        $availableVersions = [];
        foreach ($moduleVersions as $version) {
            if ($semver = Version::pepToSemver($version)) {
                $availableVersions[$semver] = $version;
            }
        }
        if (!$availableVersions) {
            $this->consoleIO?->output(<<<EOT
Python module <comment>$module</comment> not found suitable version in pip.

Read more about <comment>https://pypi.org/search</comment>
EOT
            );
            throw new CommandFailedException('Failed.');
        }
        return $availableVersions;
    }

    /**
     * pip安装模块
     *
     * @param array $modules
     * @return void
     */
    private function pipModulesInstall(array $modules): void
    {
        // 生成 requirements.txt 且安装
        $installModulesContent = '';
        foreach ($modules as $module => $version) {
            $installModulesContent .= "$module==$version\n";
        }
        System::putFileContent($requirementsFile = System::getcwd() . '/requirements.txt', $installModulesContent, cache: false);
        $this->consoleIO->subOutput(<<<EOT
Installs: 
$installModulesContent
EOT
        );
        if ($pipGlobalIndex = $this->config->get('config.pip-index-url')) {
            $this->process->executePip("config set global.index-url $pipGlobalIndex");
        }
        if ($this->process->executePip("install -r $requirementsFile", subOutput: true) !== 0) {
            throw new CommandFailedException('Failed.');
        }
    }
}
