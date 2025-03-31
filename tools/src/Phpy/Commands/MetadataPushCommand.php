<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use PhpyTool\Phpy\Application;
use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\Exceptions\CommandFailedException;
use PhpyTool\Phpy\Exceptions\CommandStopException;
use PhpyTool\Phpy\Exceptions\CommandSuccessedException;
use PhpyTool\Phpy\Helpers\PythonMetadata;
use PhpyTool\Phpy\Helpers\System;
use PhpyTool\Phpy\Installers\ModuleInstaller;
use Symfony\Component\Console\Helper\ProgressBar;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Question\ConfirmationQuestion;

class MetadataPushCommand extends AbstractCommand
{

    /** @inheritdoc  */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('metadata:push')
            ->setDescription('Push metadata');
    }

    /** @inheritdoc  */
    protected function handler(): int
    {
        $pushed = [];
        while (1) {
            $metadata = $this->consoleIO?->ask(
                "Please enter the metadata information in the format: <info>[top_level]:[module_name]</info>"
            );
            $metadataArray = explode(':', $metadata);
            if (count($metadataArray) !== 2) {
                $this->consoleIO?->error("Invalid metadata information. $metadata");
                continue;
            }
            list($topLevel, $moduleName) = $metadataArray;
            $pushed[$topLevel] = $moduleName;
            $continue = $this->consoleIO?->ask(
                "Is there anything else? [<comment>Y,n</comment>]",
                true,
                questionClass: ConfirmationQuestion::class
            );
            if (!$continue) {
                break;
            }
        }
        if (!$pushed) {
            return $this->consoleIO?->success('No metadata information entered.');
        }
        $count = count($pushed);
        // 输出 $pushed 的内容供用户确认
        $this->consoleIO?->output("Metadata to be pushing ($count):");
        foreach ($pushed as $topLevel => $moduleName) {
            $this->consoleIO?->subOutput(
                "<info>top_level</info>: <comment>$topLevel</comment> <info>module_name</info>: <comment>$moduleName</comment>"
            );
        }
        // 确认是否继续
        $confirm = $this->consoleIO?->ask(
            'Do you want to proceed with pushing the metadata? [<comment>Y,n</comment>]',
            true,
            questionClass: ConfirmationQuestion::class
        );
        if (!$confirm) {
            return $this->consoleIO?->comment('Cancelled.');
        }
        $bar = new ProgressBar($this->consoleIO?->getOutput(), count($pushed));
        $this->consoleIO?->output('Start pushing metadata.');
        foreach ($pushed as $topLevel => $moduleName) {
            PythonMetadata::pushMetadata($topLevel, $moduleName);
            $bar->advance();
        }
        $bar->finish();
        $bar->clear();
        return $this->consoleIO?->success('completed.');
    }
}
