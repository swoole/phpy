<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Installers;

use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\ConsoleIO;
use PhpyTool\Phpy\Exceptions\CommandFailedException;
use PhpyTool\Phpy\Exceptions\PhpyException;
use PhpyTool\Phpy\Helpers\Process;
use PhpyTool\Phpy\Helpers\System;
use Symfony\Component\Console\Question\ConfirmationQuestion;

class PythonInstaller implements InstallerInterface
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

    /**
     * @var string|null
     */
    protected static null|string $python = null;

    /**
     * @var string|null
     */
    protected static null|string $pip = null;


    public function __construct(Config $config, null|ConsoleIO $consoleIO = null)
    {
        $this->config = $config;
        $this->consoleIO = $consoleIO;
        $this->process = $consoleIO?->getExtra('process') ?: new Process($consoleIO);
        if (!$config->get('python')) {
            $this->skipInfo = 'Python not configured. Skip install.';
            return;
        }
        if ($pythonInstallPath = $config->get('python.install-path', '/usr/bin/python')){
            if (file_exists($pythonInstallPath)) {
                $this->skipInfo = "Python already installed at $pythonInstallPath.";
                return;
            }
        }
    }

    /** @inheritdoc  */
    public function install(): void
    {
        $version = $this->config->get('python.version', 'latest');
        $cacheDir = $this->config->get('config.cache-dir');
        $installDir = $this->config->get('python.install-dir');

        if (!$this->skipInfo) {
            $url = $this->config->get('python.source-url');
            $versionOpt = ($version === 'latest') ? '' : "--branch $version";
            // 下载源码
            $sourceDir = "$cacheDir/python-$version";
            if (!file_exists($sourceDir)) {
                $this->consoleIO?->output('CPython-source Downloading ...');
                if ($this->process->execWithProgress(
                        "git clone --depth 1 $versionOpt $url $sourceDir"
                    ) !== 0) {
                    throw new CommandFailedException('Error downloading Python.');
                }
                $this->consoleIO?->output('CPython-source Downloaded.');
            }

            // 编译安装
            $pythonInstallConfigure = $this->config->get('python.install-configure', []);
            $pythonInstallConfigure[] = "--prefix=$installDir";
            $pythonInstallConfigure = implode(' ', $pythonInstallConfigure);
            $this->consoleIO?->output("Building and installing Python-$version...");
            if (
                $this->process->execWithProgress(
                    "cd $sourceDir && ./configure $pythonInstallConfigure && make clean && make && make install"
                ) !== 0
            ) {
                throw new CommandFailedException("Error building and installing Python-$version.");
            }
        }

        $python = $installDir . '/bin/python';
        $pip = $installDir . '/bin/pip';
        $cwd = System::getcwd();
        // 虚拟环境
        if (!file_exists($venvPath = "$cwd/py-vendor/.venv")) {
            // 安装虚拟
            $this->process->execWithProgress("$python -m venv $venvPath");
            $this->process->execWithProgress("source $venvPath/bin/activate");
            // 软链python-config
            $pythonConfigPath = "$venvPath/bin/python-config";
            $this->process->execWithProgress("ln -s $installDir/bin/python-config $pythonConfigPath");
            // 软链python-include
            $this->process->execWithProgress("rm -rf $venvPath/include/python");
            $this->process->execWithProgress("ln -s $installDir/include/python $venvPath/include");
            // 设置环境
            $this->process->execWithProgress("echo '$python' > $cwd/python.command && echo '$pip' > $cwd/pip.command && echo '' > $cwd/python-config.command");
        }
    }

    /** @inheritdoc  */
    public function uninstall(): void
    {
        $version = $this->config->get('python.version', 'latest');
        $cacheDir = $this->config->get('config.cache-dir');
        // 卸载源码
        $sourceDir = "$cacheDir/python-$version";
        if (file_exists($sourceDir)) {
            $this->process->exec("rm -rf $sourceDir");
        }
        // 卸载虚拟环境
        $cwd = System::getcwd();
        if (file_exists($venvPath = "$cwd/py-vendor/.venv")) {
            $this->process->exec("rm -rf $venvPath");
        }
    }

    /** @inheritdoc  */
    public function upgrade(): void
    {
        $version = $this->config->get('python.version', 'latest');
        $cacheDir = $this->config->get('config.cache-dir');
        $installDir = $this->config->get('python.install-dir');

        if (!$this->skipInfo) {
            $url = $this->config->get('python.source-url');
            $versionOpt = ($version === 'latest') ? '' : "--branch $version";
            // 下载源码
            $sourceDir = "$cacheDir/python-$version";
            if (file_exists($sourceDir)) {
                $this->process->exec("rm -rf $sourceDir");
            }
            $this->consoleIO?->output('CPython-source Downloading ...');
            if ($this->process->execWithProgress(
                    "git clone --depth 1 $versionOpt $url $sourceDir"
                ) !== 0) {
                throw new CommandFailedException('Error downloading Python.');
            }
            $this->consoleIO?->output('CPython-source Downloaded.');

            // 编译安装
            $pythonInstallConfigure = $this->config->get('python.install-configure', []);
            $pythonInstallConfigure[] = "--prefix=$installDir";
            $pythonInstallConfigure = implode(' ', $pythonInstallConfigure);
            $this->consoleIO?->output("Building and installing Python-$version...");
            if (
                $this->process->execWithProgress(
                    "cd $sourceDir && ./configure $pythonInstallConfigure && make clean && make && make install"
                ) !== 0
            ) {
                throw new CommandFailedException("Error building and installing Python-$version.");
            }
        }

        $python = $installDir . '/bin/python';
        $pip = $installDir . '/bin/pip';
        $cwd = System::getcwd();
        // 虚拟环境
        if (file_exists($venvPath = "$cwd/py-vendor/.venv")) {
            $this->process->exec("rm -rf $venvPath");
        }
        // 安装虚拟
        $this->process->execWithProgress("$python -m venv $venvPath");
        $this->process->execWithProgress("source $venvPath/bin/activate");
        // 软链python-config
        $pythonConfigPath = "$venvPath/bin/python-config";
        $this->process->execWithProgress("ln -s $installDir/bin/python-config $pythonConfigPath");
        // 软链python-include
        $this->process->execWithProgress("rm -rf $venvPath/include/python");
        $this->process->execWithProgress("ln -s $installDir/include/python $venvPath/include");
        // 设置环境
        $this->process->execWithProgress("echo '$python' > $cwd/python.command && echo '$pip' > $cwd/pip.command && echo '' > $cwd/python-config.command");
    }

    /** @inheritdoc  */
    public function clearCache(): void
    {
        $cacheDir = $this->config->get('config.cache-dir');
        if ($this->process->execWithProgress(
            "rm -rf $cacheDir/python-*"
        ) !== 0) {
            throw new CommandFailedException('Error clearing Python cache.');
        }
    }
}
