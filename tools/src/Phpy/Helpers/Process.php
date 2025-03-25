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
     * 执行命令
     *
     * @param string $command 执行命令
     * @param array|null $output stdout & stderr （结果列表始终为倒序）
     * @param bool $subOutput 是否输出到subOutput（输出始终为正序）
     * @return int 错误码 -1失败
     */
    public function execute(string $command, ?array &$output = null, bool $subOutput = false): int
    {
        $command = str_ends_with($command, ' 2>&1') ? $command : "$command 2>&1";
        $this->debugMode("execute( $command )");
        $resultCode = -1;
        $output = $output === null ? [] : $output;
        if (is_resource($handle = popen($command, 'r'))) {
            // 逐行读取命令输出
            while (!feof($handle)) {
                $line = fgets($handle);
                if ($line !== false) {
                    $line = $line ? trim($line) : null;
                    if ($line) {
                        array_unshift($output, $line);
                        if ($subOutput) {
                            $this->consoleIO?->subOutput($line);
                        }
                    }
                }
            }
            $resultCode = pclose($handle);
        }
        return $resultCode;
    }

    /**
     * 执行命令pip
     *
     * @param string $command
     * @param mixed|null $output
     * @param bool $subOutput
     * @return int|null
     */
    public function executePip(string $command, ?array &$output = null, bool $subOutput = false): int|null
    {
        $pip = System::pip();
        return $this->execute("$pip $command", $output, subOutput: $subOutput);
    }

    /**
     * 执行命令python
     *
     * @param string $command
     * @param mixed|null $output
     * @param bool $subOutput
     * @return int|null
     */
    public function executePython(string $command, ?array &$output = null, bool $subOutput = false): int|null
    {
        $python = System::python();
        return $this->execute("$python $command", $output, subOutput: $subOutput);
    }

    /**
     * 执行命令python-config
     *
     * @param string $command
     * @param mixed|null $output
     * @param bool $subOutput
     * @return int|null
     */
    public function executePythonConfig(string $command, ?array &$output = null, bool $subOutput = false): int|null
    {
        $python = System::pythonConfig();
        return $this->execute("$python $command", $output, subOutput: $subOutput);
    }
}
