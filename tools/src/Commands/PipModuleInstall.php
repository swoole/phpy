<?php

declare(strict_types=1);

namespace PhpyTool\Commands;

use Symfony\Component\Console\Helper\QuestionHelper;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Question\Question;

class PipModuleInstall extends AbstractCommand
{
    protected string $pythonVersion = '3.10';

    /** @inheritdoc  */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('install:pip-module')
            ->setDescription('Installs Python PyORC module.')
            ->addArgument('module', InputArgument::REQUIRED, 'The module name to install')
            ->addArgument('version', InputArgument::OPTIONAL, 'The version of Python module to install', 'latest');
    }

    /** @inheritdoc  */
    protected function handler(): int
    {
        $helper = new QuestionHelper();
        $module = $this->getInput()?->getArgument('module');
        $version = $this->getInput()?->getArgument('version');

        $question = new Question("[?] Please specify the path of Python (default: /usr/bin/python3): \n", '/usr/bin/python3');
        $pythonPath = $helper->ask($this->getInput(), $this->getOutput(), $question);
        if (
            !file_exists($pythonPath) or
            version_compare(
                $this->pythonVersion = substr($this->exec("$pythonPath --version", ignore: true), 7, 4),
                '3.10',
                '<'
            )
        ) {
            return $this->error('Please install Python 3.10+ manually.');
        }

        $question = new Question("[?] Please specify the path of pip (default: /usr/bin/pip3): \n", '/usr/bin/pip3');
        $pipPath = $helper->ask($this->getInput(), $this->getOutput(), $question);
        if (!file_exists($pipPath)) {
            return $this->error('Please install Python-pip manually.');
        }

        $this->output("Installing Python module $module-$version ...");
        $moduleInstalled = $this->exec("$pipPath show $module", ignore: true);
        if (!$moduleInstalled or ($version !== 'latest' and !str_contains($moduleInstalled, "Version: $version"))) {
            if ($this->execWithProgress(
                "$pipPath install $module" . ($version === 'latest' ? '' : "==$version") . ' --break-system-packages'
            )) {
                return $this->error("Error installing Python module $module-$version.");
            }
        } else {
            $this->comment("Python module $module-$version is already installed.");
        }

        return $this->success("Python module $module-$version installation complete.");
    }
}
