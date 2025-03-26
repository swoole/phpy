<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Helpers;

use PhpyTool\Phpy\Exceptions\PhpyException;

class System
{

    /**
     * @var array<string, string>
     */
    protected static array $fileContentCache = [];

    /**
     * @var array
     */
    protected static array $existingPackages = [];

    /**
     * @return false|string
     */
    public static function getcwd()
    {
        return $GLOBALS['PHPY_CWD'] ?? getcwd();
    }

    /**
     * @param string $cwd
     * @return void
     */
    public static function setcwd(string $cwd)
    {
        $GLOBALS['PHPY_CWD'] = $cwd;
    }

    /**
     * 获取/设置 python所在路径
     *
     * @param string|null $path
     * @return string
     */
    public static function python(?string $path = null): string
    {
        if (file_exists($command = System::getcwd() . '/python.command')) {
            return trim(System::getFileContent($command));
        }
        if (!$path or !file_exists($path)) {
            if (!$path = exec('command -v python')) {
                throw new PhpyException('Python not found. ');
            }
        }
//        System::putFileContent($command, $path);
        return $path;
    }

    /**
     * 获取/设置 pip所在路径
     *
     * @param string|null $path
     * @return string
     */
    public static function pip(?string $path = null): string
    {
        if (file_exists($command = System::getcwd() . '/pip.command')) {
            return trim(System::getFileContent($command));
        }
        if (!$path or !file_exists($path)) {
            if (!$path = exec('command -v pip')) {
                throw new PhpyException('Python-pip not found. ');
            }
        }
//        System::putFileContent($command, $path);
        return $path;
    }

    /**
     * 获取/设置 python-config所在路径
     *
     * @param string|null $path
     * @return string
     */
    public static function pythonConfig(?string $path = null): string
    {
        if (file_exists($command = System::getcwd() . '/python-config.command')) {
            return trim(System::getFileContent($command));
        }
        if (!$path or !file_exists($path)) {
            if (!$path = exec('command -v python-config')) {
                throw new PhpyException('Python-config not found. ');
            }
        }
//        System::putFileContent($command, $path);
        return $path;
    }

    /**
     * 获取文件内容
     *
     * @param string $filePath
     * @param bool $cache
     * @return string
     */
    public static function getFileContent(string $filePath, bool $cache = true): string
    {
        if ($cache) {
            return static::$fileContentCache[$filePath] ??= file_get_contents($filePath);
        }
        return file_get_contents($filePath);
    }

    /**
     * 写入文件内容
     *
     * @param string $filePath
     * @param string $content
     * @param int $flag
     * @param bool $cache
     * @return bool|int
     */
    public static function putFileContent(string $filePath, string $content, int $flag = 0, bool $cache = true): bool|int
    {
        if (!$cache or $flag !== 0) {
            unset(static::$fileContentCache[$filePath]);
        } else {
            static::$fileContentCache[$filePath] = $content;
        }
        return file_put_contents($filePath, $content, $flag);
    }

    /**
     * 清除文件内容缓存
     *
     * @return void
     */
    public static function clearFileContentCache(): void
    {
        static::$fileContentCache = [];
    }


    /**
     * 获取系统类型
     *
     * @return string
     */
    public static function getPackageManager(): string
    {
        return match (true) {
            file_exists('/etc/alpine-release')                   => 'apk',
            file_exists('/etc/centos-release') ||
            file_exists('/etc/redhat-release') ||
            file_exists('/etc/fedora-release')                   => 'yum',
            file_exists('/etc/arch-release')                     => 'pacman',
            file_exists('/etc/SuSE-release')                     => 'zypper',
            stripos(php_uname('s'), 'Darwin') !== false     => 'brew',
            stripos(php_uname('s'), 'Windows') !== false    => 'winget',
            default                                                      => 'apt-get',
        };
    }

    /**
     * @return string[]
     */
    public static function getBuildToolsList(): array
    {
        return match (static::getPackageManager()) {
            'apk' => [
                'gcc', 'g++', 'make', 'autoconf',
                'musl-dev',
                'expat-dev',
                'libffi-dev',
                'openssl-dev',
                'zlib-dev',
                'xz-dev',
                'bzip2-dev',
                'sqlite-dev',
                'gdbm-dev',
                'gmp-dev',
                'pcre-dev',
                'icu-dev'
            ],
            'apt-get' => [
                'build-essential',
                'libexpat1-dev',
                'libffi-dev',
                'libssl-dev',
                'zlib1g-dev',
                'libbz2-dev',
                'libsqlite3-dev',
                'libgdbm-dev',
                'liblzma-dev',
                'libgmp-dev',
                'linux-headers-generic'
            ],
            'yum' => [
                'gcc',
                'gcc-c++',
                'make',
                'autoconf',
                'expat-devel',
                'libffi-devel',
                'openssl-devel',
                'zlib-devel',
                'bzip2-devel',
                'sqlite-devel',
                'gdbm-devel',
                'gmp-devel',
                'kernel-headers'
            ],
            'zypper' => [
                'gcc',
                'gcc-c++',
                'make',
                'autoconf',
                'libexpat-devel',
                'libffi-devel',
                'libopenssl-devel',
                'zlib-devel',
                'bzip2-devel',
                'sqlite3-devel',
                'gdbm-devel',
                'gmp-devel',
                'kernel-default-devel'
            ],
            'pacman' => [
                'gcc',
                'make',
                'autoconf',
                'expat',
                'libffi',
                'openssl',
                'zlib',
                'bzip2',
                'sqlite',
                'gdbm',
                'gmp',
                'linux-headers'
            ],
            'brew'           => ['autoconf'],
            'winget'         => ['make', 'autoconf'],
            default          => [],
        };
    }

    /**
     * 获取系统编译依赖卸载命令
     *
     * @return string|null
     */
    public static function getBuildToolsUninstall(): ?string
    {
        $uninstallPackages = array_diff(static::getBuildToolsList(), static::$existingPackages);
        static::$existingPackages = [];
        return match (static::getPackageManager()) {
            'apk'     => 'apk del ' . implode(' ', $uninstallPackages),
            'yum'     => 'sudo yum remove ' . implode(' ', $uninstallPackages),
            'brew'    => 'brew uninstall ' . implode(' ', $uninstallPackages),
            'zypper'  => 'sudo zypper remove ' . implode(' ', $uninstallPackages),
            'pacman'  => 'sudo pacman -R ' . implode(' ', $uninstallPackages),
            'winget'  => 'winget uninstall ' . implode(' ', $uninstallPackages),
            'apt-get' => 'sudo apt-get install ' . implode(' ', $uninstallPackages),
            default   => null,
        };
    }

    /**
     * 获取系统编译依赖安装命令
     *
     * @param bool $check
     * @return string|null
     */
    public static function getBuildToolsInstall(bool $check = true): ?string
    {
        $packages = static::getBuildToolsList();
        self::$existingPackages = $check ? self::checkExistingPackages($packages) : [];

        $installPackages = array_diff($packages, self::$existingPackages);
        if (!$installPackages) {
            return null;
        }
        return match (self::getPackageManager()) {
            'apk'     => 'apk add --no-cache ' . implode(' ', $installPackages),
            'yum'     => 'sudo yum install ' . implode(' ', $installPackages),
            'brew'    => 'brew install ' . implode(' ', $installPackages),
            'zypper'  => 'sudo zypper install ' . implode(' ', $installPackages),
            'pacman'  => 'sudo pacman -S ' . implode(' ', $installPackages),
            'winget'  => 'winget install ' . implode(' ', $installPackages),
            'apt-get' => 'sudo apt-get install ' . implode(' ', $installPackages),
            default   => null,
        };
    }

    /**
     * 检查系统中已存在的包
     *
     * @param array $packages
     * @return array
     */
    protected static function checkExistingPackages(array $packages): array
    {
        $existingPackages = [];
        foreach ($packages as $package) {
            $result = match (self::getPackageManager()) {
                'apk'    => shell_exec("apk info | grep ^$package\$"),
                'yum'    => shell_exec("rpm -q $package"),
                'brew'   => shell_exec("brew list --formula | grep ^$package\$"),
                'zypper' => shell_exec("zypper se -i | grep ^$package\$"),
                'pacman' => shell_exec("pacman -Qi $package"),
                'winget' => shell_exec("winget list $package"),
                default  => shell_exec("dpkg -l | grep ^ii | grep $package") ||
                    shell_exec("apt list --installed | grep ^$package/"),
            };

            if ($result and !empty(trim($result))) {
                $existingPackages[] = $package;
            }
        }
        return $existingPackages;
    }
}
