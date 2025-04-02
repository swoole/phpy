<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Helpers;

use PhpyTool\Phpy\ConsoleIO;
use PhpyTool\Phpy\Exceptions\PhpyException;

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
     *  - 默认将stderr重定向合并至stdout
     *  - command支持使用2>，自定义stderr重定向
     *      - 2>/dev/null： 忽略stderr
     *      - 2>&1： 合并stderr至stdout
     *      - 2>/tmp/run.log： 将stderr重定向至文件
     *
     * @param string $command 执行命令
     * @param array|null $output stdout & stderr （结果列表始终为倒序）
     * @param bool $subOutput 是否输出到subOutput（输出始终为正序）
     * @return int 错误码 -1失败
     */
    public function execute(string $command, ?array &$output = null, bool $subOutput = false): int
    {
        $command = str_contains($command, ' 2>') ? $command : "$command 2>&1";
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

    /**
     * 请求
     *  - 当未安装curl拓展时尝试使用curl命令执行http请求
     *
     * @param string $method
     * @param string $url
     * @param array $data
     * @param array $headers
     * @return array{httpCode:int, responseBody:string}
     */
    public function request(string $method, string $url, array $data = [], array $headers = []): array
    {
        $method = strtoupper($method);
        $headers['Accept'] ??= 'application/json';
        // 统一处理 GET 参数
        if ($method === 'GET') {
            $url .= $data
                ? (str_contains($url, '?') ? '&' : '?') . http_build_query($data)
                : '';
        } else {
            $jsonData = json_encode($data, JSON_UNESCAPED_UNICODE);
            $headers['Content-Type'] = 'application/json';
            $headers['Content-Length'] = strlen($jsonData);
        }
        // 没有安装curl，则使用curl命令
        if (!extension_loaded('curl')) {
            return $this->requestUseCurlShell($method, $url, $data, $headers);
        }
        $ch = curl_init();
        try {
            $options = [
                CURLOPT_URL             => $url,
                CURLOPT_RETURNTRANSFER  => true,
                CURLOPT_CUSTOMREQUEST   => $method,
                CURLOPT_HTTPHEADER      => self::formatHeaders($headers),
                CURLOPT_FOLLOWLOCATION  => true,
                CURLOPT_CONNECTTIMEOUT  => 30,
                CURLOPT_TIMEOUT         => 60,
            ];
            if (isset($jsonData)) {
                $options[CURLOPT_POSTFIELDS] = $jsonData;
            }
            curl_setopt_array($ch, $options);
            $responseBody = curl_exec($ch);
            if ($errorNo = curl_errno($ch)) {
                throw new PhpyException("cURL error ($errorNo): " . curl_error($ch), $errorNo);
            }
            $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            return [
                'httpCode'      => (int)$httpCode,
                'responseBody'  => (string)$responseBody
            ];
        } finally {
            curl_close($ch);
        }
    }

    /**
     * 使用curl命令请求
     *
     * @param string $method
     * @param string $url
     * @param array $data
     * @param array $headers
     * @return array{httpCode:int, responseBody:string}
     */
    public function requestUseCurlShell(string $method, string $url, array $data = [], array $headers = []): array
    {
        $method = strtoupper($method);
        $cmd = [
            'curl',
            '-sS',
            '-X', $method,
            '-o', '-',
            '-w', "HTTP_CODE=%{http_code}",
            '--connect-timeout', '30',
            '--max-time', '60'
        ];
        // 添加请求头
        foreach (self::formatHeaders($headers) as $header) {
            array_push($cmd, '-H', escapeshellarg($header));
        }

        // 处理请求体
        if ($method !== 'GET' and $data) {
            $jsonData = json_encode($data, JSON_UNESCAPED_UNICODE);
            array_push($cmd, '--data', escapeshellarg($jsonData));
        }

        $cmd[] = escapeshellarg($url);
        $output = [];
        $resultCode = $this->execute(implode(' ', $cmd), $output);
        // 处理命令行执行错误
        if ($resultCode !== 0) {
            throw new PhpyException("cURL command failed (exit $resultCode): " . implode("\n", $output), $resultCode);
        }
        $rawResponse = implode('', array_reverse($output));
        if (preg_match('/^(?<response_body>.*)HTTP_CODE=(?<http_code>\d+)$/s', $rawResponse, $matches)) {
            return [
                'httpCode' => (int)$matches['http_code'],
                'responseBody' => (string)$matches['response_body']
            ];
        } else {
            throw new PhpyException("Invalid response format: $rawResponse");
        }
    }

    /**
     * headers map to headers
     *
     * @param array $headers
     * @return array
     */
    private static function formatHeaders(array $headers): array
    {
        return array_map(
            fn($k, $v) => "$k: $v",
            array_keys($headers),
            array_values($headers)
        );
    }

}
