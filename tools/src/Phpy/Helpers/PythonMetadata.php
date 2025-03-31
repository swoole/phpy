<?php

namespace PhpyTool\Phpy\Helpers;

use PhpyTool\Phpy\Exceptions\PhpyException;

class PythonMetadata
{
    /** @var string  */
    protected static string $apiKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRmYmpnbnBtdGx6eXRiZXp3dGR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDI5ODQ5MjQsImV4cCI6MjA1ODU2MDkyNH0.trmgSPSI55IRnU4ko1E6gJQNi-kyXbobsl61bkRZVBE';

    /**
     * 判断是否是标准库
     *
     * @param string $module
     * @return bool
     */
    public static function isStdLibrary(string $module): bool
    {
        static $stdLibrary = null;
        if (!$stdLibrary) {
            $stdLibrary = array_flip(self::getPythonStdModules());
        }
        return isset($stdLibrary[$module]);
    }

    /**
     * 通过系统函数获取python标准库
     *
     * @return array
     */
    public static function getPythonStdModules(): array
    {
        $pythonCode = <<<'PYTHON'
import sys, json
print(json.dumps(sorted(sys.stdlib_module_names)))
PYTHON;
        // 执行命令并捕获输出
        (new Process())->executePython("-c '$pythonCode'", $output);
        return json_decode($output[0], true) ?? [];
    }

    /**
     * 上报metadata
     *
     * @param string $topLevel
     * @param string $moduleName
     * @param string $version
     * @return array
     */
    public static function pushMetadata(string $topLevel, string $moduleName, string $version = 'default'): array
    {
        $res = (new Process())->request(
            'POST',
            "https://tfbjgnpmtlzytbezwtdx.supabase.co/rest/v1/rpc/push_metadata",
            [
                'p_module_name' => $moduleName,
                'p_top_level'   => $topLevel,
                'p_version'     => $version
            ],
            [
                'Content-Type'  => 'application/json',
                'apikey'        => static::$apiKey,
                'Authorization' => 'Bearer ' . static::$apiKey
            ]
        );
        if ($res['httpCode'] !== 200) {
            throw new PhpyException("push metadata failed: {$res['responseBody']}");
        }
        return json_decode($res['responseBody'], true) ?? [];
    }

    /**
     * 根据topLevel查询对应的模块信息
     *
     * @param string $topLevel
     * @param int $limit
     * @return array
     */
    public static function queryByTopLevel(string $topLevel, int $limit = 0): array
    {
        $res = (new Process())->request(
            'POST',
            "https://tfbjgnpmtlzytbezwtdx.supabase.co/rest/v1/rpc/query_by_top_level",
            [
                'p_top_level'   => $topLevel,
                'p_limit'       => $limit
            ],
            [
                'Content-Type'  => 'application/json',
                'apikey'        => static::$apiKey,
                'Authorization' => 'Bearer ' . static::$apiKey
            ]
        );
        if ($res['httpCode'] !== 200) {
            throw new PhpyException("push metadata failed: {$res['responseBody']}");
        }
        return json_decode($res['responseBody'], true) ?? [];
    }


    /**
     * 根据topLevel查询对应的模块信息
     *
     * @param string $nameString
     * @param string $version
     * @return string|null
     */
    static function getPipPackage(string $nameString, string $version = 'default'): ?string
    {
        static $metadataMap = [];
        [$topLevel] = explode('.', $nameString);
        if (!isset($metadataMap[$topLevel])) {
            $moduleName = null;
            if ($query = static::queryByTopLevel($topLevel)) {
                foreach ($query as $item) {
                    if ($version === $item['version']) {
                        $moduleName = $item['module_name'];
                        break;
                    }
                }
            }
            $metadataMap[$topLevel] = $moduleName;
        }
        return $metadataMap[$topLevel] ?? null;
    }
}