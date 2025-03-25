<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\Exceptions\CommandFailedException;
use PhpyTool\Phpy\Exceptions\CommandStopException;
use PhpyTool\Phpy\Exceptions\CommandSuccessedException;
use PhpyTool\Phpy\Installers\BuildToolsInstaller;
use PhpyTool\Phpy\Installers\PhpyInstaller;
use Symfony\Component\Console\Helper\QuestionHelper;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Question\ConfirmationQuestion;

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
        $config = new Config();
        $pythonSourceUrl = $config->get('phpy.source-url', 'https://github.com/swoole/phpy.git');
        $config->set('phpy.source-url', $this->consoleIO?->ask(
            "Please enter the ext-phpy source code URL to install (default: <comment>$pythonSourceUrl</comment>).",
            $pythonSourceUrl
        ));

        $pythonVersion = $config->get('phpy.install-version', 'latest');
        $config->set('phpy.install-version', $this->consoleIO?->ask(
            "Please enter the ext-phpy version to install (default: <comment>$pythonVersion</comment>).",
            $pythonVersion
        ));

        if ($this->consoleIO?->ask(
            'Do you want to add ext-phpy in php.ini? [<comment>Y,n</comment>]:',
            false,
            questionClass: ConfirmationQuestion::class
        )) {
            $phpyIniPath = $config->get('phpy.ini-path', '/usr/local/etc/php/conf.d/xx-php-ext-phpy.ini');
            $config->set('phpy.ini-path', $this->consoleIO?->ask(
                "Please enter the ext-phpy php.ini path (default: <comment>$phpyIniPath</comment>).",
                $phpyIniPath
            ));
        } else {
            $config->set('phpy.ini-path', null);
        }
        try {
            $buildTools = new BuildToolsInstaller($config, $this->consoleIO);
            $buildTools->install();
            (new PhpyInstaller($config, $this->consoleIO))->install();
            if ($this->consoleIO?->ask(
                'Do you need to uninstall the build dependencies? [<comment>n,Y</comment>]',
                false,
                questionClass: ConfirmationQuestion::class
            )) {
                $buildTools->uninstall();
            }
        } catch (CommandStopException) {
            return $this->consoleIO?->success('Installation stop.');
        } catch (CommandSuccessedException $exception) {
            return $this->consoleIO?->success($exception->getMessage());
        } catch (CommandFailedException $exception) {
            return $this->consoleIO?->error($exception->getMessage());
        }

        return $this->consoleIO?->success('PHPy installation completed. ');
    }
}
