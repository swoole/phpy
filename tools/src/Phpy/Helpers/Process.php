<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Helpers;

use PhpyTool\Phpy\ConsoleIO;

class Process
{
    /**
     * @var ConsoleIO|null
     */
    protected ConsoleIO|null $consoleIO;

    /**
     * @var bool
     */
    protected bool $debug;

    /**
     * @var string
     */
    protected string $runtimeId;

    public function __construct(ConsoleIO|null $consoleIO = null, string|null $runtimeId = null, bool $debug = false)
    {
        $this->runtimeId = $runtimeId ?: uniqid();
        $this->consoleIO = $consoleIO;
        $this->debug = $debug;
    }

    /**
     * @return string
     */
    public function getRuntimeId(): string
    {
        return $this->runtimeId;
    }

    /**
     * @param string $info
     * @return void
     */
    private function debugMode(string $info): void
    {
        if ($this->debug) {
            $this->consoleIO?->subOutput($info = "DEBUG INFO -> $info");
            $file = str_replace('\\', '_', get_called_class()) . '-' . $this->runtimeId;
            if (!is_dir($dir = getcwd() . "/.log")) {
                mkdir($dir, 0777, true);
            }
            file_put_contents("$dir/$file.log", "$info\n", FILE_APPEND | LOCK_EX);
        }
    }

    /**
     * @param string $command
     * @param null|mixed $lastLine
     * @return string|int|bool|null
     */
    public function pipExec(string $command, mixed &$lastLine = null): string|int|bool|null
    {
        $pip = System::pip();
        return $this->execWithProgress("$pip $command", $lastLine);
    }

    /**
     * @param string $command
     * @param null|mixed $lastLine
     * @return bool|int|string|null
     */
    public function pythonExec(string $command, mixed &$lastLine = null): bool|int|string|null
    {
        $python = System::python();
        return $this->execWithProgress("$python $command", $lastLine);
    }

    /**
     * @param string $command
     * @param null|mixed $lastLine
     * @return bool|int|string|null
     */
    public function pythonConfigExec(string $command, mixed &$lastLine = null): bool|int|string|null
    {
        $python = System::pythonConfig();
        return $this->execWithProgress("$python $command", $lastLine);
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
    public function exec(string $command, mixed &$output = null, mixed &$resultCode = 0, bool $ignore = false): string|int|bool|null
    {
        $this->debugMode("exec( $command )");
        $lastLine = exec($command, $output, $resultCode);
        if ($resultCode !== 0 and !$ignore) {
            $this->consoleIO?->error($lastLine);
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
    public function system(string $command, ?int &$resultCode = 0, bool $ignore = false): string|int|bool|null
    {
        $this->debugMode("system( $command )");
        $info = system($command, $resultCode);
        if ($resultCode !== 0) {
            if (!$ignore) {
                $this->consoleIO?->error($info);
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
    public function execWithProgress(string $command, ?string &$lastLine = null): int
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
                    $this->consoleIO?->subOutput($lastLine);
                }
            }
            usleep(1000);
        }
        $this->debugMode("> rc: null | last info: $lastLine");
        return pclose($process);
    }
}
