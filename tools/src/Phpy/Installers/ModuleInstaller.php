<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Installers;

use Composer\Semver\Semver;
use PhpyTool\Phpy\Application;
use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\ConsoleIO;
use PhpyTool\Phpy\Exceptions\CommandFailedException;
use PhpyTool\Phpy\Helpers\Process;
use PhpyTool\Phpy\Helpers\System;

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
        if (!$config->get('module')) {
            $this->skipInfo = 'Module not configured. Skip install.';
            return;
        }
    }

    /**
     * 查询 pip 库中的模块版本
     *
     * @param string $module
     * @return array|null
     */
    protected function moduleVersions(string $module): ?array
    {
        $res = $this->process->pipExec("index versions $module");
        if (!str_contains($res, 'ERROR')) {
            // 解析 pip 输出，获取模块的可用版本
            preg_match_all('/Available versions: (.+)/', $res, $matches);
            return explode(', ', $matches[1][0] ?? '');
        }
        return null;
    }

    /** @inheritdoc  */
    public function install(): void
    {
        $modules = $this->config->get('modules', []);
        $installModules = [];
        foreach ($modules as $module => $versionConstraint) {
            // 查询 pip 库中的模块版本
            if (!$availableVersions = $this->moduleVersions($module)) {
                $this->consoleIO?->output(<<<EOT
Python module <comment>$module</comment> not found in pip.

Read more about <comment>https://pypi.org/search</comment>
EOT
                );
                throw new CommandFailedException('Install failed.');
            }
            // 检查版本是否满足约束
            $satisfyingVersions = Semver::satisfiedBy($availableVersions, $versionConstraint);
            if (!$satisfyingVersions) {
                $this->consoleIO?->output(<<<EOT
Python module <info>$module</info> version <comment>$versionConstraint</comment>> not found in pip.

Read more about <comment>https://pypi.org/search</comment>
EOT
                );
                throw new CommandFailedException('Install failed.');
            }
            // 选择满足约束的版本
            $installModules[$module] = Semver::rsort($satisfyingVersions);
        }

        // 没有hash，说明是json文件安装，则扫描vendor
        if (!$this->config->get('hash')) {
            // vendor
            $vendorModules = [];
            Application::getVendorConfigFiles(function ($organization, $package, $configFilePath) use (&$vendorModules) {
                $config = new Config($configFilePath);
                $modules = $config->get('modules', []);
                foreach ($modules as $module => $versionConstraint) {
                    $vendorModules[$module][$versionConstraint] = [
                        'organization' => $organization,
                        'package' => $package,
                    ];
                }
            });
            foreach ($vendorModules as $module => $item) {
                // others
                if (!isset($installModules[$module])) {
                    // 查询 pip 库中的模块版本
                    if (!$availableVersions = $this->moduleVersions($module)) {
                        $this->consoleIO?->output(<<<EOT
Python module <info>$module</info> not found in pip.

Read more about <comment>https://pypi.org/search</comment>
EOT
                        );
                        throw new CommandFailedException('Install failed.');
                    }
                }
                // exits
                else {
                    $availableVersions = $installModules[$module];
                }
                foreach ($item as $versionConstraint => $info) {
                    // 检查版本是否满足约束
                    $satisfyingVersions = Semver::satisfiedBy($availableVersions, $versionConstraint);
                    if (!$satisfyingVersions) {
                        $this->consoleIO?->output(<<<EOT
Package <info>{$info['organization']}/{$info['package']}</info> --
Python module <info>$module</info> version-constraint <comment>$versionConstraint</comment>> not found in pip.

Read more about <comment>https://pypi.org/search</comment>
EOT
                        );
                        throw new CommandFailedException('Install failed.');
                    }
                    $availableVersions = Semver::rsort($satisfyingVersions);
                }
                $installModules[$module] = $availableVersions;
            }
        }
        if ($installModules) {
            // 生成 requirements.txt 且安装
            $installModulesContent = '';
            foreach ($installModules as $module => $versions) {
                $this->config->set("modules.$module", $version = $versions[0]);
                $installModulesContent .= "$module==$version\n";
            }
            System::putFileContent($requirementsFile = System::getcwd() . '/requirements.txt', $installModulesContent, cache: false);
            $this->consoleIO->subOutput(<<<EOT
Installs: 
$installModulesContent
EOT);
            if ($pipGlobalIndex = $this->config->get('config.pip-index-url')) {
                $this->process->pipExec("config set global.index-url $pipGlobalIndex");
            }
            if ($this->process->pipExec("install -r $requirementsFile") !== 0) {
                throw new CommandFailedException('Install failed.');
            }
        } else {
            $this->consoleIO->output('No modules to install.');
        }
    }

    /** @inheritdoc  */
    public function uninstall(): void
    {
    }

    /** @inheritdoc  */
    public function upgrade(): void
    {
        $modules = $this->config->get('modules', []);
        $this->config->set('local-modules', $modules);
        $installModules = [];
        foreach ($modules as $module => $versionConstraint) {
            // 查询 pip 库中的模块版本
            if (!$availableVersions = $this->moduleVersions($module)) {
                $this->consoleIO?->output(<<<EOT
Python module <comment>$module</comment> not found in pip.

Read more about <comment>https://pypi.org/search</comment>
EOT
                );
                throw new CommandFailedException('Update failed.');
            }
            // 检查版本是否满足约束
            $satisfyingVersions = Semver::satisfiedBy($availableVersions, $versionConstraint);
            if (!$satisfyingVersions) {
                $this->consoleIO?->output(<<<EOT
Python module <info>$module</info> version-constraint <comment>$versionConstraint</comment>> not found in pip.

Read more about <comment>https://pypi.org/search</comment>
EOT
                );
                throw new CommandFailedException('Update failed.');
            }
            // 选择满足约束的版本
            $installModules[$module] = Semver::rsort($satisfyingVersions);
        }
        // vendor
        $vendorModules = [];
        Application::getVendorConfigFiles(function ($organization, $package, $configFilePath) use (&$vendorModules) {
            $config = new Config($configFilePath);
            $modules = $config->get('modules', []);
            foreach ($modules as $module => $versionConstraint) {
                $vendorModules[$module][$versionConstraint] = [
                    'organization' => $organization,
                    'package' => $package,
                ];
            }
        });
        foreach ($vendorModules as $module => $item) {
            // others
            if (!isset($installModules[$module])) {
                // 查询 pip 库中的模块版本
                if (!$availableVersions = $this->moduleVersions($module)) {
                    $this->consoleIO?->output(<<<EOT
Python module <info>$module</info> not found in pip.

Read more about <comment>https://pypi.org/search</comment>
EOT
                    );
                    throw new CommandFailedException('Update failed.');
                }
            }
            // exits
            else {
                $availableVersions = $installModules[$module];
            }
            foreach ($item as $versionConstraint => $info) {
                // 检查版本是否满足约束
                $satisfyingVersions = Semver::satisfiedBy($availableVersions, $versionConstraint);
                if (!$satisfyingVersions) {
                    $this->consoleIO?->output(<<<EOT
Package <info>{$info['organization']}/{$info['package']}</info> --
Python module <info>$module</info> version-constraint <comment>$versionConstraint</comment>> not found in pip.

Read more about <comment>https://pypi.org/search</comment>
EOT
                    );
                    throw new CommandFailedException('Update failed.');
                }
                $availableVersions = Semver::rsort($satisfyingVersions);
            }
            $installModules[$module] = $availableVersions;
        }
        if ($installModules) {
            // 生成 requirements.txt 且安装
            $installModulesContent = '';
            foreach ($installModules as $module => $versions) {
                $this->config->set("modules.$module", $version = $versions[0]);
                $installModulesContent .= "$module==$version\n";
            }
            System::putFileContent($requirementsFile = System::getcwd() . '/requirements.txt', $installModulesContent, cache: false);
            $this->consoleIO->subOutput(<<<EOT
Updates: 
$installModulesContent
EOT);
            if ($pipGlobalIndex = $this->config->get('config.pip-index-url')) {
                $this->process->pipExec("config set global.index-url $pipGlobalIndex");
            }
            if ($this->process->pipExec("install -r $requirementsFile") !== 0) {
                throw new CommandFailedException('Update failed.');
            }
        }
        $this->config->set('vendor-modules', $vendorModules);
    }

    /** @inheritdoc  */
    public function clearCache(): void
    {
    }
}
