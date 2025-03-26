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
     * @var null|string
     */
    protected null|string $skipInfo = null;

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
     * 查询 pip 库中的模块版本
     *
     * @param string $module
     * @return array|null
     */
    public function moduleVersions(string $module): ?array
    {
        $resultCode = $this->process->executePip("index versions $module", output: $output);
        if ($resultCode === 0) {
            $res = [];
            foreach ($output as $line) {
                if (str_starts_with($line, 'Available versions:')) {
                    // 解析 pip 输出，获取模块的可用版本
                    preg_match_all('/Available versions: (.+)/', $line, $matches);
                    $res = explode(', ', $matches[1][0] ?? '');
                }
            }
            return $res;
        }
        return null;
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
        foreach ($dirs as $dir) {

            if (!is_dir($dir = System::getcwd() . $dir)) {
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
        $modules = [];
        foreach ($packages as $key => $package) {
            $package = explode('.', $package)[0];
            if (PythonMetadata::isStdLibrary($package)) {
                continue;
            }
            if ($availableVersions = $this->moduleVersions($package)) {
                $modules[$package] = Semver::rsort($availableVersions)[0];
            }
        }
        if ($modules) {
            $count = count($modules);
            $this->consoleIO?->output("Installs: $count");
            foreach ($modules as $module => $version) {
                $this->consoleIO?->subOutput("<comment>--</comment> <info>$module</info> - <comment>$version</comment>");
            }
        }
        if (!$this->consoleIO?->ask(
            "Do you want to install these modules? [<comment>Y,n</comment>]",
            true,
            ConfirmationQuestion::class
        )) {
            throw new CommandStopException('PHPy will not install any modules');
        }
        $this->config->set('modules', array_merge($this->config->get('modules', []), $modules));
    }

    /** @inheritdoc  */
    public function install(): void
    {
        $this->consoleIO?->output('Installing/Updating modules ...');
        $modules = $this->config->get('modules', []);
        $vendorModules = $this->config->get('vendor-modules', []);
        $phpyHash = $this->config->get('phpy-hash');
        $composerHash = $this->config->get('composer-hash');

        // 如果存在 phpy-hash 和 composer-hash， 则为install
        if ($phpyHash and $composerHash) {
            $installModules = array_merge($modules, $vendorModules);
        }
        // 不存在，则为update
        else {
            $this->config->set('phpy-hash', hash_file('SHA256', System::getcwd() . '/phpy.json'));
            $this->config->set('composer-hash', hash_file('SHA256', System::getcwd() . '/composer.json'));
            $localModules = [];
            foreach ($modules as $module => $versionConstraint) {
                $localModules[$module] = $this->satisfyingVersions($module, $this->availableVersions($module), $versionConstraint);
            }

            // vendor
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

            $vendorModules = [];
            foreach ($vendors as $module => $item) {
                $availableVersions = ($local = isset($localModules[$module]))
                    ? $localModules[$module]
                    : $this->availableVersions($module);
                // 循环检查所有组织/包的版本约束
                foreach ($item as $versionConstraint => $info) {
                    $availableVersions = $this->satisfyingVersions($module, $availableVersions, $versionConstraint, $info);
                }
                if ($availableVersions) {
                    if (!$local) {
                        $vendorModules[$module] = $availableVersions[0];
                    } else {
                        $localModules[$module] = $availableVersions[0];
                    }
                }
            }
            $this->config->set('modules', $localModules);
            $this->config->set('vendor-modules', $vendorModules);
            $installModules = array_merge($localModules, $vendorModules);
        }

        if ($installModules) {
            $this->pipModulesInstall($installModules);
        } else {
            $this->consoleIO->output('No modules.');
        }
    }

    /** @inheritdoc  */
    public function uninstall(): void
    {
    }

    /** @inheritdoc  */
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

    /** @inheritdoc  */
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
     * @param array $availableVersions
     * @param string $versionConstraint
     * @param array<string, string> $info
     * @return array
     */
    private function satisfyingVersions(string $module, array $availableVersions, string $versionConstraint, array $info = []): array
    {
        $organization = $info['organization'] ?? null;
        $package = $info['package'] ?? null;
        $msg = ($organization and $package)
            ? "Package <info>{$info['organization']}/{$info['package']}</info>"
            : "Local";
        // 检查版本是否满足约束
        $satisfyingVersions = Semver::satisfiedBy($availableVersions, $versionConstraint);
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
     * @return array
     */
    public function availableVersions(string $module): array
    {
        // 查询 pip 库中的模块版本
        if (!$availableVersions = $this->moduleVersions($module)) {
            $this->consoleIO?->output(<<<EOT
Python module <comment>$module</comment> not found in pip.

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
EOT);
        if ($pipGlobalIndex = $this->config->get('config.pip-index-url')) {
            $this->process->executePip("config set global.index-url $pipGlobalIndex");
        }
        if ($this->process->executePip("install -r $requirementsFile", subOutput: true) !== 0) {
            throw new CommandFailedException('Failed.');
        }
    }
}
