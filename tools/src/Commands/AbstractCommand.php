<?php

declare(strict_types=1);

namespace PhpyTool\Commands;

use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Formatter\OutputFormatterStyle;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Output\OutputInterface;

abstract class AbstractCommand extends Command
{
    public static bool $debug = false;

    /**
     * @var OutputInterface|null
     */
    protected ?OutputInterface $output = null;

    /**
     * @var InputInterface|null
     */
    protected ?InputInterface $input = null;

    /**
     * @var string|null
     */
    protected ?string $runtimeId = null;

    /**
     * @return void
     */
    protected function configure(): void
    {
        $this->addOption('debug', null, InputOption::VALUE_NONE, 'Enable debug mode.');
    }

    /**
     * @return OutputInterface|null
     */
    public function getOutput(): ?OutputInterface
    {
        return $this->output;
    }

    /**
     * @return InputInterface|null
     */
    public function getInput(): ?InputInterface
    {
        return $this->input;
    }

    /**
     * @return string|null
     */
    public function getRuntimeId(): ?string
    {
        return $this->runtimeId;
    }

    /**
     * @param string $info
     * @return void
     */
    private function debugMode(string $info): void
    {
        if (self::$debug) {
            $this->subOutput($info = "DEBUG INFO -> $info");
            $file = str_replace('\\', '_', get_called_class()) . '-' . $this->getRuntimeId();
            if (!is_dir($dir = getcwd() . "/.log")) {
                mkdir($dir, 0777, true);
            }
            file_put_contents("$dir/$file.log", "$info\n", FILE_APPEND | LOCK_EX);
        }
    }

    /**
     * 执行命令
     *
     * @param string $command
     * @param mixed|null $output
     * @param int|null $resultCode
     * @param bool $ignore 忽略中断
     * @return string|int|bool|null
     */
    protected function exec(string $command, mixed &$output = null, mixed &$resultCode = 0, bool $ignore = false): string|int|bool|null
    {
        $this->debugMode("exec( $command )");
        $lastLine = exec($command, $output, $resultCode);
        if ($resultCode !== 0 and !$ignore) {
            $this->error($lastLine);
            return $resultCode;
        }
        $this->debugMode("->> rc: $resultCode | last info: $lastLine");
        return $lastLine;
    }

    /**
     * @param string $command
     * @param int|null $resultCode
     * @param bool $ignore
     * @return string|int|bool|null
     */
    protected function system(string $command, ?int &$resultCode = 0, bool $ignore = false): string|int|bool|null
    {
        $this->debugMode("system( $command )");
        $info = system($command, $resultCode);
        if ($resultCode !== 0) {
            if (!$ignore) {
                $this->error($info);
                return $resultCode;
            }
        }
        $this->debugMode("->> rc: $resultCode | last info: $info");
        return $info;
    }

    /**
     * @param string $command
     * @param string|null $lastLine
     * @return int resultCode
     */
    protected function execWithProgress(string $command, ?string &$lastLine = null): int
    {
        $this->debugMode("execWithProgress( $command )");
        $process = popen($command, 'r');
        while (!feof($process)) {
            $line = fgets($process);
            if ($line === false) {
                break;
            } else {
                $lastLine = trim($line);
                if ($lastLine) {
                    $this->subOutput($lastLine);
                }
            }
            usleep(1000);
        }
        $this->debugMode("> rc: null | last info: $lastLine");
        return pclose($process);
    }

    /**
     * sub输出
     *
     * @param string $message
     * @param string $tag
     * @return void
     */
    protected function subOutput(string $message, string $tag = '[>]'): void
    {
        $this->getOutput()?->getFormatter()->setStyle('sub-output', new OutputFormatterStyle('gray', null, ['underscore']));
        $this->getOutput()?->writeln("$tag <sub-output>$message</sub-output>");
    }

    /**
     * 普通输出
     *
     * @param string $message
     * @param string $tag
     * @return void
     */
    protected function output(string $message, string $tag = '[>]'): void
    {
        $this->getOutput()?->writeln("$tag $message");
    }

    /**
     * 输出info
     *
     * @param string $message
     * @return void
     */
    protected function comment(string $message): void
    {
        $this->getOutput()?->writeln("[i] <comment>$message</comment>");
    }

    /**
     * 输出error
     *
     * @param string $message
     * @return int
     */
    protected function error(string $message): int
    {
        $this->getOutput()?->writeln("[×] <error>$message</error>");
        return self::FAILURE;
    }

    /**
     * 输出success
     *
     * @param string $message
     * @return int
     */
    protected function success(string $message): int
    {
        $this->getOutput()?->writeln("[√] <info>$message</info>");
        return self::SUCCESS;
    }

    /** @inheritdoc  */
    final protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $this->runtimeId = uniqid();
        $this->input = $input;
        $this->output = $output;
        if (self::$debug = $input->getOption('debug')) {
            $this->comment("Run in debug mode. ID: {$this->getRuntimeId()}");
        }
        return $this->handler();
    }

    /**
     * @return int
     */
    abstract protected function handler(): int;

}
