<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\Exceptions\CommandFailedException;
use PhpyTool\Phpy\Exceptions\CommandStopException;
use PhpyTool\Phpy\Exceptions\CommandSuccessedException;
use PhpyTool\Phpy\Installers\BuildToolsInstaller;
use PhpyTool\Phpy\Installers\PythonInstaller;
use Symfony\Component\Console\Helper\QuestionHelper;
use Symfony\Component\Console\Input\InputOption;

class PythonInstall extends AbstractCommand
{

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
        $config = new Config();
        $pythonSourceUrl = $config->get('python.source-url', 'https://github.com/python/cpython.git');
        $config->set('python.source-url', $this->consoleIO?->ask(
            "Please enter the Python source code URL to install (default: <comment>$pythonSourceUrl</comment>).",
            $pythonSourceUrl
        ));

        $pythonVersion = $config->get('python.install-version', 'latest');
        $config->set('python.install-version', $this->consoleIO?->ask(
            "Please enter the Python version to install (default: <comment>$pythonVersion</comment>).",
            $pythonVersion
        ));

        $pythonInstallDir = $config->get('python.install-dir', '/usr');
        $config->set('python.install-dir', $this->consoleIO?->ask(
            "Please enter the Python installation directory (default: <comment>$pythonInstallDir</comment>).",
            $pythonInstallDir
        ));

        try {
            $buildTools = new BuildToolsInstaller($config, $this->consoleIO);
            $buildTools->install();
            (new PythonInstaller($config, $this->consoleIO))->install();
            if ($this->consoleIO?->ask(
                'Do you need to uninstall the build dependencies? [<comment>n,Y</comment>]',
                false,
                questionClass: QuestionHelper::class
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
        return $this->consoleIO?->success('Python installation complete.');
    }
}
