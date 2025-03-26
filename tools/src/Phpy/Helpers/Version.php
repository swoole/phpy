<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Helpers;

use Composer\Semver\VersionParser;

class Version
{

    /**
     * @param string $version
     * @return bool
     */
    public static function validateVersion(string $version): bool {
        try {
            VersionParser::parseStability($version);
            (new VersionParser())->normalize($version);
            return true;
        } catch (\UnexpectedValueException) {
            return false;
        }
    }

    /**
     * @param string $version
     * @return int[]
     */
    public static function splitVersion(string $version): array {
        $cleanVer = ltrim(strtolower($version), 'v');
        preg_match('/^(\d+)(?:\.(\d+))?(?:\.(\d+))?/', $cleanVer, $matches);

        return [
            (int)($matches[1] ?? 0),
            (int)($matches[2] ?? 0),
            (int)($matches[3] ?? 0)
        ];
    }

}
