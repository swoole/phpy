<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\Exceptions\CommandFailedException;
use PhpyTool\Phpy\Exceptions\CommandStopException;
use PhpyTool\Phpy\Exceptions\CommandSuccessedException;
use PhpyTool\Phpy\Helpers\PackageCollector;
use PhpyTool\Phpy\Helpers\PythonMetadata;
use PhpyTool\Phpy\Installers\BuildToolsInstaller;
use PhpyTool\Phpy\Installers\ModuleInstaller;
use RecursiveDirectoryIterator;
use RecursiveIteratorIterator;
use Symfony\Component\Console\Helper\QuestionHelper;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Question\ConfirmationQuestion;

class ScanImport extends AbstractCommand
{
    /** @inheritdoc */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('scan:import')
            ->setDescription('Scan the code to see what python modules are imported.')
            ->addArgument('path', InputArgument::REQUIRED, 'The path to scan.');
    }

    private function findPhpFiles($directory): array
    {
        $phpFiles = [];
        $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory));
        foreach ($iterator as $file) {
            if ($file->isFile() && pathinfo($file->getFilename(), PATHINFO_EXTENSION) === 'php') {
                $phpFiles[] = $file->getPathname();
            }
        }
        return $phpFiles;
    }

    /** @inheritdoc */
    protected function handler(): int
    {
        $this->consoleIO?->output('Scan the PHP code in the path directory to see what Python modules are imported ...');
        $srcPath = realpath($this->consoleIO?->getInput()->getArgument('path'));
        if (!is_dir($srcPath)) {
            return $this->consoleIO?->error('The path is not a directory.');
        }

        try {
            $config = new Config();
            $config->set('config.scan-dirs', [$srcPath]);
            $moduleInstaller = new ModuleInstaller($config, $this->consoleIO);
            $moduleInstaller->scan();

            if ($config->get('modules')) {
                $buildTools = new BuildToolsInstaller($config, $this->consoleIO);
                if ($this->consoleIO?->ask(
                    'Do you want to install the dependent packages? [<comment>Y,n</comment>]',
                    true,
                    questionClass: ConfirmationQuestion::class
                )) {
                    $buildTools->install();
                    $moduleInstaller->install();
                }
                if ($this->consoleIO?->ask(
                    'Do you need to uninstall the build dependencies? [<comment>n,Y</comment>]',
                    false,
                    questionClass: ConfirmationQuestion::class
                )) {
                    $buildTools->uninstall();
                }
            }
        } catch (CommandStopException) {
            return $this->consoleIO?->success('Stop.');
        } catch (CommandSuccessedException $exception) {
            return $this->consoleIO?->success($exception->getMessage());
        } catch (CommandFailedException $exception) {
            return $this->consoleIO?->error($exception->getMessage());
        }
        return $this->consoleIO?->success('Scan import complete.');
    }
}
