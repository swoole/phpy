<?php

namespace PhpyTool\Commands;

use PhpyTool\PackageCollector;
use PhpyTool\PythonMetadata;
use RecursiveDirectoryIterator;
use RecursiveIteratorIterator;
use Symfony\Component\Console\Helper\QuestionHelper;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Question\ConfirmationQuestion;
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
        $this->output('Scan the PHP code in the path directory to see what Python modules are imported ...');
        $srcPath = realpath($this->input->getArgument('path'));
        if (!is_dir($srcPath)) {
            return $this->error('The path is not a directory.');
        }

        $files = $this->findPhpFiles($srcPath);
        $packages = [];
        foreach ($files as $file) {
            $this->output->writeln('Scanning <info>' . str_replace($srcPath . '/', '', $file) . '</info>');
            $packages = array_merge($packages, PackageCollector::parseFile($file));
        }

        $packages = array_unique($packages);
        if (!$packages) {
            $this->output('No Python modules found.');
            return 0;
        }

        $packages = array_filter($packages, function ($module) {
            return !PythonMetadata::isStdLibrary($module);
        });
        $this->output('Found Python modules: ' . implode(', ', array_map(function ($module) {
                return "<comment>$module</comment>";
            }, $packages)));

        $helper = new QuestionHelper();
        $question = new ConfirmationQuestion("[?] Should the dependent packages be written into <info>requirements.txt</info> (yes/no)?: \n", false);
        if ($helper->ask($this->getInput(), $this->getOutput(), $question)) {
            $pipPackages = array_unique(array_filter(array_map(function ($module) {
                return PythonMetadata::getPipPackage($module);
            }, $packages), fn($package) => $package !== null));

            $requirementsFile = 'requirements.txt';

            $original = file_get_contents($requirementsFile);
            $lines = explode("\n", $original);
            foreach ($lines as $line) {
                [$_package] = explode('==', $line);
                if (in_array($_package, $pipPackages)) {
                    unset($pipPackages[array_search($_package, $pipPackages)]);
                }
            }

            $fp = fopen($requirementsFile, 'a');
            fwrite($fp, "\n" . implode("\n", $pipPackages));
            fclose($fp);

            $this->success("The dependent packages have been written to <info>$requirementsFile</info>.");

            if ($helper->ask($this->getInput(), $this->getOutput(), new ConfirmationQuestion("[?] Do you want to install the dependent packages (yes/no)?: \n", false))) {
                $this->output('Installing dependent packages ...');
                system('pip install -r ' . $requirementsFile);
                return $this->success('The dependent packages have been installed.');
            }
        }
        return 0;
    }
}
