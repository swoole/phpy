<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Helpers;

use Composer\Semver\VersionParser;
use PhpyTool\Phpy\Exceptions\PhpyException;

class Version
{

    /**
     * 获取模块的PEP可用版本列表
     *
     * @param string $module
     * @return array
     */
    public static function getPepVersions(string $module): array
    {
        static $modulePepVersions = [];
        if (!isset($modulePepVersions[$module])) {
            $retry = 0;
            do {
                try {
                    $res = (new Process())->request(
                        'GET',
                        "https://pypi.org/pypi/$module/json",
                        [],
                        [
                            'Content-Type' => 'application/json'
                        ]
                    );
                } catch (\Throwable) {
                    echo "request error, retry $retry";
                    usleep(($retry + 1 ) * 200 * 1000);
                } finally {
                    $retry ++;
                }
            } while ($retry < 3);

            $httpCode = $res['httpCode'] ?? 500;

            $res = json_decode($responseBody = $res['responseBody'], true);
            if ($httpCode === 404) {
                $modulePepVersions[$module] = [];
            } else if ($httpCode === 200) {
                $modulePepVersions[$module] = array_keys($res['releases'] ?? []);
            } else {
                throw new PhpyException("Request failed: $responseBody");
            }
        }
        return $modulePepVersions[$module] ?? [];
    }

    /**
     * 将符合 PEP 440 稳定版格式（含有限预发行标识）的版本号转换为 SemVer 格式。
     *
     * 规则说明：
     * 1. 如果版本中包含 epoch（例如 "1!1.2.3"）或 post-release（例如 "1.2.3.post1"），返回 null。
     * 2. 仅支持纯数字部分和预发行部分（预发行部分仅允许 a/alpha、b/beta、rc），格式必须完全符合要求。
     * 3. 数字部分：若不足三段，则补 0；若超过三段，则将第三段及以后部分合并为 patch，
     *    如 "2.3.4.5" 转换为 "2.3.45"。
     * 4. 预发行部分转换为 SemVer 格式，形式为 "-<label>.<number>"。不支持 dev、pre 等其它标识，遇到则返回 null。
     *
     * @param string $pepVersion 输入的 PEP 440 版本字符串
     * @return string|null 转换后的 SemVer 版本字符串；对于不兼容的情况返回 null
     */
    public static function pepToSemver(string $pepVersion): ?string
    {
        // 去除左右空白，并移除前导 "v" 或 "V"
        if (stripos($version = trim($pepVersion), 'v') === 0) {
            $version = substr($version, 1);
        }
        // step1 忽略epoch和post-release
        if (
            str_contains($version, '!') or
            stripos($version, 'post') !== false
        ) {
            return null;
        }
        // step2 匹配数字部分和预发行部分
        $pattern = '/^(\d+(?:\.\d+)*)(?:([a-zA-Z]+)(\d+))?$/';
        if (!preg_match($pattern, $version, $matches)) {
            return null;
        }
        // step3 数字部分
        $parts = explode('.', $matches[1]);
        // 保证至少x.y.z，不足补0
        while (count($parts) < 3) {
            $parts[] = '0';
        }
        // 超出则合并z及以后为new-z
        if (count($parts) > 3) {
            $patchParts = array_slice($parts, 2);
            $parts[2] = implode('', $patchParts);
        }
        // 仅取前三部分作为 major、minor、patch 构成 SemVer
        $semver = "$parts[0].$parts[1].$parts[2]";
        // step4 检查是否存在预发行部分
        if ($matches[2] ?? '') {
            $preLabelRaw = strtolower($matches[2]);
            $preNum = $matches[3] ?? '';
            // 使用 match 表达式处理预发行标签，仅允许 a/alpha, b/beta, rc，其它返回 null
            $preLabel = match ($preLabelRaw) {
                'a', 'alpha'    => 'alpha',
                'b', 'beta'     => 'beta',
                'rc'            => 'rc',
                default         => null,
            };
            if (!$preLabel) {
                return null;
            }
            $semver .= "-$preLabel.$preNum";
        }

        return $semver;
    }


    /**
     * 校验版本
     *
     * @param string $version 版本字符串
     * @param bool $isPepVersion 是否pep440
     * @return bool
     */
    public static function validatePepVersion(string $version, bool $isPepVersion = true): bool
    {
        $semverVersion = $isPepVersion ? static::pepToSemver($version) : $version;
        try {
            VersionParser::parseStability($semverVersion);
            (new VersionParser())->normalize($semverVersion);
            return true;
        } catch (\UnexpectedValueException) {
            return false;
        }
    }

    /**
     * 切割版本
     *
     * @param string $semverVersion
     * @return int[]
     */
    public static function splitVersion(string $semverVersion): array {
        $cleanVer = ltrim(strtolower($semverVersion), 'v');
        preg_match('/^(\d+)(?:\.(\d+))?(?:\.(\d+))?/', $cleanVer, $matches);

        return [
            (int)($matches[1] ?? 0),
            (int)($matches[2] ?? 0),
            (int)($matches[3] ?? 0)
        ];
    }

}
