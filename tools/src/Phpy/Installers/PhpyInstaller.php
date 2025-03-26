<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Installers;

use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\ConsoleIO;
use PhpyTool\Phpy\Exceptions\CommandFailedException;
use PhpyTool\Phpy\Helpers\Process;
use PhpyTool\Phpy\Helpers\System;

class PhpyInstaller implements InstallerInterface
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
        if (!$config->get('phpy')) {
            $this->skipInfo = 'PHPy not configured. Skip install.';
            return;
        }
        if (extension_loaded('phpy')){
            $this->skipInfo = "PHPy already installed.";
            return;
        }
    }

    /** @inheritdoc  */
    public function install(): void
    {
        if ($this->skipInfo) {
            $this->consoleIO?->comment($this->skipInfo);
            return;
        }
        $this->consoleIO?->output('PHPy Installing/Upgrading ...');
        $url = $this->config->get('phpy.source-url');
        $version = $this->config->get('phpy.install-version', 'latest');
        $cacheDir = $this->config->get('config.cache-dir');
        if (str_starts_with($cacheDir, '~')) {
            $cacheDir = str_replace('~', getenv('HOME'), $cacheDir);
        }
        $versionOpt = ($version === 'latest') ? '' : "--branch $version";
        // 下载源码
        $sourceDir = "$cacheDir/phpy-$version";
        if (!file_exists($sourceDir)) {
            $this->consoleIO?->output('PHPy-source Downloading ...');
            if ($this->process->execute(
                    "git clone --depth 1 $versionOpt $url $sourceDir", subOutput: true
                ) !== 0) {
                throw new CommandFailedException('Error downloading PHPy-source.');
            }
            $this->consoleIO?->output('PHPy-source Downloaded.');
        }
        // 编译安装
        $pythonConfigDir = System::pythonConfig();
        $phpyInstallConfigure = $this->config->get('phpy.install-configure') ?: [
            "--with-python-config=$pythonConfigDir"
        ];
        $phpyInstallConfigure = implode(' ', $phpyInstallConfigure);
        $phpIniPath = $this->config->get('phpy.ini-path');
        $iniCmd = $phpIniPath ? "&& echo 'extension=phpy.so' > $phpIniPath" : '';
        if (
            $this->process->execute(
                "cd $sourceDir && phpize && ./configure $phpyInstallConfigure && make clean && make && make install $iniCmd",
                subOutput: true
            ) !== 0
        ) {
            throw new CommandFailedException('Error building and installing PHPy extension.');
        }
    }

    /** @inheritdoc  */
    public function uninstall(): void
    {
        $this->consoleIO?->output('PHPy Uninstalling ...');
        $phpIniPath = $this->config->get('phpy.ini-path');
        if (file_exists($phpIniPath)) {
            $this->process->execute("rm $phpIniPath", subOutput: true);
        }
    }

    /** @inheritdoc  */
    public function upgrade(): void
    {
        $this->skipInfo = null;
        $this->install();
    }

    /** @inheritdoc  */
    public function clearCache(): void
    {
        $cacheDir = $this->config->get('config.cache-dir');
        if (str_starts_with($cacheDir, '~')) {
            $cacheDir = str_replace('~', getenv('HOME'), $cacheDir);
        }
        if ($this->process->execute(
            "rm -rf $cacheDir/phpy-*", subOutput: true
        ) !== 0) {
            throw new CommandFailedException('Error clearing PHPy cache.');
        }
    }
}
