<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Installers;

use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\ConsoleIO;
use PhpyTool\Phpy\Exceptions\CommandFailedException;
use PhpyTool\Phpy\Helpers\Process;
use PhpyTool\Phpy\Helpers\System;
use Symfony\Component\Console\Question\ConfirmationQuestion;

class BuildToolsInstaller implements InstallerInterface
{
    /**
     * @var Config
     */
    protected Config $config;

    /**
     * @var ConsoleIO|null
     */
    protected null|ConsoleIO $consoleIO;

    /**
     * @var Process
     */
    protected Process $process;


    public function __construct(Config $config, null|ConsoleIO $consoleIO = null)
    {
        $this->config = $config;
        $this->consoleIO = $consoleIO;
        $this->process = $consoleIO?->getExtra('process') ?: new Process($consoleIO);
    }

    /** @inheritdoc  */
    public function install(): void
    {
        $this->consoleIO?->output('Installing/Upgrading dependency tools ...');
        // 编译依赖工具
        if ($command = System::getBuildToolsInstall()) {
            if ($this->consoleIO?->ask(
                "<info>Do you want to install dependency tools?</info> <comment>$command</comment> [<comment>Y,n</comment>]",
                true,
                questionClass: ConfirmationQuestion::class
            )) {
                if ($this->process->execute(
                        "$command", subOutput: true
                    ) !== 0) {
                    throw new CommandFailedException('Error installing dependency tools.');
                }
            }
        }
    }

    /** @inheritdoc  */
    public function uninstall(): void
    {
        $this->consoleIO?->output('Uninstalling dependency tools ...');
        // 卸载编译依赖工具
        if ($command = System::getBuildToolsUninstall()) {
            if ($this->consoleIO?->ask(
                "<info>Do you want to uninstall dependency tools?</info>> <comment$command</comment> [<comment>y,N</comment>])",
                false,
                questionClass: ConfirmationQuestion::class
            )) {
                $this->process->execute(
                    "$command", subOutput: true
                );
            }
        }
    }

    /** @inheritdoc  */
    public function upgrade(): void
    {
        $this->install();
    }

    /** @inheritdoc  */
    public function clearCache(): void
    {
    }
}
