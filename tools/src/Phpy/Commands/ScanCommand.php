<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use PhpyTool\Phpy\Application;
use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\Exceptions\CommandFailedException;
use PhpyTool\Phpy\Exceptions\CommandStopException;
use PhpyTool\Phpy\Exceptions\CommandSuccessedException;
use PhpyTool\Phpy\Helpers\System;
use PhpyTool\Phpy\Installers\ModuleInstaller;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Question\ConfirmationQuestion;

class ScanCommand extends AbstractCommand
{

    /** @inheritdoc  */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('scan')
            ->addArgument('dirs', InputArgument::IS_ARRAY|InputArgument::OPTIONAL, 'Scan directories', [])
            ->setDescription('Scan python modules import and dependencies')
            ->setHelp(
                <<<EOT
The <info>scan</info> command scan python modules import and dependencies.

PHPy introduces modules through Python-pip, read more at 
https://pypi.org/help/
EOT
            );
    }

    /** @inheritdoc  */
    protected function handler(): int
    {
        $config = new Config();
        if (!$dirs = $this->consoleIO->getInput()->getArgument('dirs')) {
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
            $config->load($jsonFile);
        } else {
            $config->set('config.scan-dirs', $dirs);
        }
        try {
            $moduleInstaller = new ModuleInstaller($config, $this->consoleIO);
            // 解析 import依赖
            $moduleInstaller->scan();
            // 安装
            $moduleInstaller->upgrade();
        } catch (CommandStopException $exception) {
            return $this->consoleIO?->success($exception->getMessage() ?: 'Scan stop.');
        } catch (CommandSuccessedException $exception) {
            return $this->consoleIO?->success($exception->getMessage());
        } catch (CommandFailedException $exception) {
            return $this->consoleIO?->error($exception->getMessage());
        }
        return $this->consoleIO?->success('Scan completed.');
    }
}
