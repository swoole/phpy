<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use PhpyTool\Phpy\Application;
use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\Exceptions\CommandFailedException;
use PhpyTool\Phpy\Exceptions\CommandStopException;
use PhpyTool\Phpy\Exceptions\CommandSuccessedException;
use PhpyTool\Phpy\Helpers\System;
use PhpyTool\Phpy\Installers\BuildToolsInstaller;
use PhpyTool\Phpy\Installers\ModuleInstaller;
use PhpyTool\Phpy\Installers\PhpyInstaller;
use PhpyTool\Phpy\Installers\PythonInstaller;
use Symfony\Component\Console\Question\ConfirmationQuestion;

class InstallCommand extends AbstractCommand
{

    /** @inheritdoc  */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('install')
            ->setDescription('Installs the project dependencies from the phpy.lock file if present, or falls back on the phpy.json')
            ->addOption('skip-env', null, null, 'Skip the environment installation.')
            ->addOption('skip-ext', null, null, 'Skip the phpy extension installation.')
            ->addOption('skip-module', null, null, 'Skip the module installation.')
            ->setHelp(
                <<<EOT
The <info>install</info> command checks and installs the Python 
environment based on phpy.json, with methods like conda or venv 
configurable through the Python module in php.json. 
Use <comment>--skip-env</comment> to skip this step.

It also checks and installs phpy extensions based on phpy.json. 
The phpy version, automatic injection into php.ini, and other 
configurations can be set through the phpy module in php.json. 
Use <comment>--skip-ext</comment> to skip this step.

Finally, the command reads phpy.lock from the current 
directory to install Python module dependencies, using the 
environment specified in phpy.json to execute pip install. 
Use <comment>--skip-module</comment> to skip this step.

PHPy introduces modules through Python-pip, read more at 
https://pypi.org/help/
EOT
            );
    }

    /** @inheritdoc  */
    protected function handler(): int
    {
        try {
            // find json file
            $jsonFile = Application::findConfigFile(function ($file, $cDir, $sDir) {
                if ($cDir !== $sDir) {
                    if (!$this->consoleIO?->ask(
                        "<info>No phpy.json in current directory, do you want to use the one at $cDir</info> [<comment>Y,n</comment>]?",
                        true,
                        ConfirmationQuestion::class
                    )) {
                        throw new CommandStopException("PHPy could not find a phpy.json file in $sDir");
                    }
                }
                System::setcwd($cDir);
            });
            if (!$jsonFile) {
                throw new CommandFailedException('PHPy could not find a phpy.json file in the project');
            }
            // 尝试读取lock
            if (!$lockFile = Application::getLockFile(System::getcwd())) {
                $this->consoleIO?->comment("No phpy.lock file present. Updating dependencies to latest instead of installing from lock file.");
            }
            $config = new Config($lockFile ?: $jsonFile);
            // build tools
            (new BuildToolsInstaller($config, $this->consoleIO))->install();
            // install python env
            if (!$this->consoleIO?->getInput()->getOption('skip-env')) {
                (new PythonInstaller($config, $this->consoleIO))->install();
            }
            // install phpy extensions
            if (!$this->consoleIO?->getInput()->getOption('skip-ext')) {
                (new PhpyInstaller($config, $this->consoleIO))->install();
            }
            // install modules
            if (!$this->consoleIO?->getInput()->getOption('skip-module')) {
                // module
                (new ModuleInstaller($config, $this->consoleIO))->install();
            }
            if (!$lockFile) {
                Application::setLockFile(System::getcwd(), $config->all());
            }

        } catch (CommandStopException) {
            return $this->consoleIO?->success('Installation stop.');
        } catch (CommandSuccessedException $exception) {
            return $this->consoleIO?->success($exception->getMessage());
        } catch (CommandFailedException $exception) {
            return $this->consoleIO?->error($exception->getMessage());
        }
        return $this->consoleIO?->success('Installation completed.');
    }
}
