<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use PhpyTool\Phpy\ConsoleIO;
use PhpyTool\Phpy\Helpers\Process;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Output\OutputInterface;

abstract class AbstractCommand extends Command
{
    /**
     * @var ConsoleIO|null
     */
    protected ConsoleIO|null $consoleIO = null;

    /**
     * @var Process|null
     */
    protected Process|null $process = null;

    /**
     * @return void
     */
    protected function configure(): void
    {
        $this->addOption('debug', null, InputOption::VALUE_NONE, 'Enable debug mode.');
    }

    /**
     * @return string|null
     */
    public function getRuntimeId(): ?string
    {
        return $this->process?->getRuntimeId();
    }

    /**
     * @return Process|null
     */
    public function getProcess(): ?Process
    {
        return $this->process;
    }

    /**
     * @return ConsoleIO|null
     */
    public function getConsoleIO(): ?ConsoleIO
    {
        return $this->consoleIO;
    }

    /** @inheritdoc  */
    final protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $this->consoleIO = new ConsoleIO($input, $output, $this->getHelperSet());
        $this->process = new Process($this->consoleIO, uniqid(), (bool)$input->getOption('debug'));
        return $this->handler();
    }

    /**
     * @return int
     */
    abstract protected function handler(): int;

}
