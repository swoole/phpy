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

class ClearCacheCommand extends AbstractCommand
{

    /** @inheritdoc  */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('clear-cache')
            ->setDescription("Clears phpy's Python-source and ext-phpy cache")
            ->setHelp(
                <<<EOT
The <info>clear-cache</info> command deletes all cached Python-source and ext-phpy from
phpy's cache directory.
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
            $config = new Config($jsonFile);
            // Python
            (new PythonInstaller($config, $this->consoleIO))->clearCache();
            // ext-phpy
            (new PhpyInstaller($config, $this->consoleIO))->clearCache();

        } catch (CommandStopException) {
            return $this->consoleIO?->success('Clear-cache stop.');
        } catch (CommandSuccessedException $exception) {
            return $this->consoleIO?->success($exception->getMessage());
        } catch (CommandFailedException $exception) {
            return $this->consoleIO?->error($exception->getMessage());
        }
        return $this->consoleIO?->success('Clear-cache completed.');
    }
}
