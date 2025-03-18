<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\Installers\ModuleInstaller;
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
            ->setDescription('Installs Python module.')
            ->addArgument('module', InputArgument::REQUIRED, 'The module name to install')
            ->addArgument('version', InputArgument::OPTIONAL, 'The version of Python module to install', 'latest');
    }

    /** @inheritdoc  */
    protected function handler(): int
    {
        $module = $this->consoleIO?->getInput()->getArgument('module');
        $version = $this->consoleIO?->getInput()?->getArgument('version');

        $moduleInstaller = new ModuleInstaller(new Config(), $this->consoleIO);
        $versions = $moduleInstaller->availableVersions($module);
        if ($version === 'latest') {
            $ver = $versions[0];
        }
        if ($index = array_search($version, $versions, true)) {
            $ver = $versions[$index];
        }
        if ($ver ?? null) {
            return $this->consoleIO?->error("Python module $module-$version is not available.");
        }
        if (
            $this->process->executePip("install $module==$version --break-system-packages", subOutput: true)
            !== 0
        ) {
            return $this->consoleIO?->error("Error installing Python module $module-$version.");
        }

        return $this->consoleIO?->success("Python module $module-$version installation complete.");
    }
}
