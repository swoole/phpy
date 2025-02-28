<?php

declare(strict_types=1);

namespace PhpyTool\Commands;

use Symfony\Component\Console\Helper\QuestionHelper;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Question\Question;

class PythonInstall extends AbstractCommand
{
    protected string $pythonVersion = '3.10';

    /** @inheritdoc  */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('install:python')
            ->setDescription('Installs Python 3.10+.')
            ->addOption('venv', null, InputOption::VALUE_NONE, 'Install virtual environment');
    }

    /** @inheritdoc  */
    protected function handler(): int
    {
        $this->output('Checking and installing Python-3.10+ Python-pip Python-dev ...');
        if (!$installCommands = $this->getPythonInstallCommands()) {
            return $this->error('Unsupported operating system.');
        }
        $this->execWithProgress($installCommands, $lastLine);
        if (!str_starts_with($lastLine, 'OK:')) {
            return $this->error('Failed to install Python-3.10+ Python-pip Python-dev.');
        }
        // 再次检查Python版本
        if (version_compare(
            $this->pythonVersion = substr($this->exec('python3 --version', ignore: true), 7, 4),
            '3.10',
            '<'
        )
        ) {
            return $this->error('Python version must be 3.10 or higher.');
        }

        // 安装虚拟环境
        if ($this->getInput()?->getOption('venv')) {
            $helper = new QuestionHelper();
            $question = new Question("[?] Please specify the path of Python-venv (default: getcwd()/.venv): \n", null);
            $venvPath = $helper->ask($this->getInput(), $this->getOutput(), $question);
            // 检查虚拟环境是否已经存在
            $venvPath = $venvPath ?: getcwd(). '/.venv';
            $this->output("Setting up virtual environment in $venvPath ...");
            if (!file_exists($venvPath)) {
                // 安装虚拟
                $this->execWithProgress("python3 -m venv $venvPath");
                $this->execWithProgress("source $venvPath/bin/activate");
                // 软链python-config
                $pythonConfigPath = "$venvPath/bin/python-config";
                $this->execWithProgress("ln -s /usr/bin/python-config $pythonConfigPath");
                // 软链python-include
                $this->execWithProgress("rm -rf $venvPath/include/python$this->pythonVersion");
                $this->execWithProgress("ln -s /usr/include/python$this->pythonVersion $venvPath/include");
                $this->output("Virtual environment created. Python-config path: $pythonConfigPath");
            } else {
                $this->comment('Virtual environment already exists.');
            }
        }

        return $this->success('Python installation complete.');
    }

    private function getPythonInstallCommands(): ?string
    {
        return match ($this->getSystemType()) {
            'alpine'    => 'apk add --no-cache python3 py3-pip python3-dev',
            'redhat'    => 'sudo yum install -y python3 python3-venv python3-pip python3-dev',
            'darwin'    => 'brew install python3',
            'windows'   => null,
            default     => 'sudo apt-get install -y python3 python3-venv python3-pip python3-dev'
        };
    }

    private function getSystemType(): string
    {
        return match (true) {
            file_exists('/etc/alpine-release')                  => 'alpine',
            file_exists('/etc/centos-release') ||
            file_exists('/etc/redhat-release')                  => 'redhat',
            stripos(php_uname('s'), 'Darwin') !== false    => 'darwin',
            stripos(php_uname('s'), 'Windows') !== false   => 'windows',
            default                                                     => 'linux',
        };
    }
}
