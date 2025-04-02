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
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Question\ConfirmationQuestion;

class UpdateCommand extends AbstractCommand
{

    /** @inheritdoc  */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('update')
            ->setDescription('Updates your dependencies to the latest version according to phpy.json, and updates the phpy.lock file')
            ->addArgument('module', InputArgument::OPTIONAL, 'Python module name to update')
            ->addOption('skip-build-tools', null, null, 'Skip the build tools installation.')
            ->addOption('skip-env', null, null, 'Skip the environment upgrade.')
            ->addOption('skip-ext', null, null, 'Skip the phpy extension upgrade.')
            ->addOption('skip-module', null, null, 'Skip the module upgrade.')
            ->setHelp(
                <<<EOT
The <info>update</info> command reads the phpy.json file from the
current directory, processes it, and updates, removes or installs all the
dependencies.

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
                        questionClass: ConfirmationQuestion::class
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
            $lockFile = Application::getLockFile(System::getcwd());
            $config = new Config($jsonFile);
            $config->merge(new Config($lockFile));
            // build tools
            if (!$this->consoleIO?->getInput()->getOption('skip-build-tools')) {
                (new BuildToolsInstaller($config, $this->consoleIO))->install();
            }
            // update python env
            if (!$this->consoleIO?->getInput()->getOption('skip-env')) {
                (new PythonInstaller($config, $this->consoleIO))->upgrade();
            }
            // install phpy extensions
            if (!$this->consoleIO?->getInput()->getOption('skip-ext')) {
                (new PhpyInstaller($config, $this->consoleIO))->upgrade();
            }
            // install modules
            if (!$this->consoleIO?->getInput()->getOption('skip-module')) {
                // module
                (new ModuleInstaller($config, $this->consoleIO))->upgrade();
            }
            Application::setLockFile(System::getcwd(), $config->all());
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
