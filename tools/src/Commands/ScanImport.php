<?php

namespace PhpyTool\Commands;

use PhpyTool\PackageCollector;
use RecursiveDirectoryIterator;
use RecursiveIteratorIterator;
use Symfony\Component\Console\Helper\QuestionHelper;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Question\Question;

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

    private function findPhpFiles($directory)
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
        $this->output('Scan the PHP code in the path directory to see what Python modules are imported ...');
        $srcPath = realpath($this->input->getArgument('path'));
        if (!is_dir($srcPath)) {
            return $this->error('The path is not a directory.');
        }

        $files = $this->findPhpFiles($srcPath);
        $packages = [];
        foreach ($files as $file) {
            $this->output->writeln('Scanning <info>' . str_replace($srcPath . '/', '', $file). '</info>');
            $packages = array_merge($packages, PackageCollector::parseFile($file));
        }

        $packages = array_unique($packages);
        if ($packages) {
            $this->output('Found Python modules: ' . implode(', ', array_map(function ($module) {
                    return "<comment>$module</comment>";
                }, $packages)));

        } else {
            $this->output('No Python modules found.');
        }
        return 0;
    }
}