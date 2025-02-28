<?php

declare(strict_types=1);

namespace PhpyTool\Commands;

use Symfony\Component\Console\Helper\QuestionHelper;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Question\ConfirmationQuestion;
use Symfony\Component\Console\Question\Question;

class PhpyInstall extends AbstractCommand
{
    /** @inheritdoc  */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('install:phpy')
            ->setDescription('Installs PHP-ext PHPy.')
            ->addArgument('version', InputArgument::OPTIONAL, 'The version of PHPy to install', 'latest');
    }

    /** @inheritdoc  */
    protected function handler(): int
    {
        $helper = new QuestionHelper();
        $version = $this->getInput()?->getArgument('version');
        // 询问安装目录
        $question = new Question("[?] Please specify the installation directory (default: .runtime): \n", getcwd() . '/.runtime');
        $installDir = $helper->ask($this->getInput(), $this->getOutput(), $question) . '/swoole_phpy_' . str_replace('.', '', $version);

        if (!file_exists($installDir)) {
            // 下载源码
            $this->output('Downloading the latest source code ...');
            if (
                $this->execWithProgress($version === 'latest' ?
                    "git clone --depth 1 https://github.com/swoole/phpy.git $installDir" :
                    "git clone --depth 1 --branch $version https://github.com/swoole/phpy.git $installDir") !== 0
            ) {
                return $this->error('Error downloading source code.');
            }
        } else {
            $this->comment('PHPy source code already downloaded.');
        }

        // 安装编译依赖组件
        $this->output('Installing dependencies...');
        if ($installCommands = $this->getSystemInstallCommands()) {
            if ($this->execWithProgress($installCommands) !== 0) {
                return $this->error('Error installing dependencies.');
            }
        } else {
            return $this->error('Please install PHPy manually.');
        }

        $question = new Question("[?] Please specify the Python-config directory (default: /usr/bin/python-config): \n", '/usr/bin/python-config');
        $pythonConfigDir = $helper->ask($this->getInput(), $this->getOutput(), $question);
        // 编译并安装拓展
        $this->output('Building and installing PHPy extension...');
        if (
            $this->execWithProgress(
                "cd $installDir && phpize && ./configure --with-python-config=$pythonConfigDir && make clean && make && make install"
            ) !== 0
        ) {
            return $this->error('Error building and installing PHPy extension.');
        }

        // 询问是否移除源码
        $question = new ConfirmationQuestion("[?] Do you want to add ext-PHPy in php.ini? [Y/n]: \n", true);
        if ($helper->ask($this->getInput(), $this->getOutput(), $question)) {
            $question = new Question("[?] Please specify the php.ini path (default: /usr/local/etc/php/conf.d/xx-php-ext-phpy.ini): \n", '/usr/local/etc/php/conf.d/xx-php-ext-phpy.ini');
            $phpIniPath = $helper->ask($this->getInput(), $this->getOutput(), $question);
            $this->system('echo "extension=phpy.so" > ' . $phpIniPath, $rc, true);
            if ($rc !== 0) {
                $this->error('Error removing source code. Your can remove it manually.');
            }
        }

        // 询问是否移除源码
        $question = new ConfirmationQuestion("[?] Do you want to remove the source code? (path: $installDir) [Y/n]: \n", true);
        if ($helper->ask($this->getInput(), $this->getOutput(), $question)) {
            $this->system('rm -rf ' . $installDir, $rc, true);
            if ($rc !== 0) {
                $this->error('Error removing source code. Your can remove it manually.');
            }
        }

        // 询问是否卸载编译依赖组件
        $question = new ConfirmationQuestion("[?] Do you want to remove the build dependencies? [Y/n]: \n", true);
        if ($helper->ask($this->getInput(), $this->getOutput(), $question)) {
            $removeCommands = $this->getSystemUninstallCommands();
            if ($removeCommands) {
                if ($this->execWithProgress($removeCommands) !== 0) {
                    $this->error('Error removing build dependencies. Your can remove it manually.');
                }
            }
        }

        // 询问是composer安装swoole/phpy
        $question = new ConfirmationQuestion("[?] Do you want to require swoole/phpy? [y/N]: \n", false);
        if ($helper->ask($this->getInput(), $this->getOutput(), $question)) {
            if ($this->execWithProgress('composer require swoole/phpy --ignore-platform-req=ext-phpy') !== 0) {
                $this->error('Error requiring PHPy via Composer. Your can require it manually.');
            }
        }

        return $this->success('PHPy installation completed successfully. ');
    }

    private function getSystemInstallCommands(): ?string
    {
        return match ($this->getSystemType()) {
            'alpine'    => 'apk add --no-cache gcc g++ make autoconf',
            'redhat'    => 'sudo yum install -y gcc gcc-c++ make autoconf',
            'darwin'    => 'brew install autoconf',
            'windows'   => null,
            default     => 'sudo apt-get install -y build-essential autoconf',
        };
    }

    private function getSystemUninstallCommands(): ?string
    {
        return match ($this->getSystemType()) {
            'alpine'    => 'apk del gcc g++ make autoconf',
            'redhat'    => 'sudo yum remove -y gcc gcc-c++ make autoconf',
            'darwin'    => 'brew uninstall autoconf',
            'windows'   => null,
            default     => 'sudo apt-get remove -y build-essential autoconf',
        };
    }

    private function getSystemType(): string
    {
        return match (true) {
            file_exists('/etc/alpine-release')                => 'alpine',
            file_exists('/etc/centos-release') ||
            file_exists('/etc/redhat-release')                => 'redhat',
            stripos(php_uname('s'), 'Darwin') !== false  => 'darwin',
            stripos(php_uname('s'), 'Windows') !== false => 'windows',
            default                                                    => 'linux',
        };
    }
}
