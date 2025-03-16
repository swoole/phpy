<?php

declare(strict_types=1);

namespace PhpyTool\Phpy;

use Closure;
use PhpyTool\Phpy\Commands\InstallCommand;
use PhpyTool\Phpy\Commands\PhpyInstall;
use PhpyTool\Phpy\Commands\PipMirrorConfig;
use PhpyTool\Phpy\Commands\PipModuleInstall;
use PhpyTool\Phpy\Commands\PythonInstall;
use PhpyTool\Phpy\Commands\ShowCommand;
use PhpyTool\Phpy\Commands\UpdateCommand;
use PhpyTool\Phpy\Helpers\System;

class Application extends \Symfony\Component\Console\Application
{
    /** @var string  */
    public const VERSION = '0.0.1';

    /** @var string  */
    private string $logo = <<<doc
  _____  _____ <comment> _____      </comment>
 |  _  ||  |  |<comment>|  _  | _ _ </comment>
 |   __||     |<comment>|   __|| | |</comment>
 |__|   |__|__|<comment>|__|   |_  |</comment>
               <comment>       |___|</comment> by <info>Swoole</info>
doc;

    public function __construct()
    {
        System::setcwd(getcwd());
        parent::__construct('PHPy', static::VERSION);
        $this->addCommands([
            new InstallCommand(),
            new UpdateCommand(),
            new ShowCommand(),
            new PipModuleInstall(),
            new PhpyInstall(),
            new PythonInstall(),
            new PipMirrorConfig(),
        ]);
    }

    /**
     * @return string
     */
    public function getLogo(): string
    {
        return $this->logo;
    }

    /** @inheritdoc  */
    public function getLongVersion(): string
    {
        return \sprintf(<<<EOT
 %s
 <info>%s</info> version <comment>%s</comment>
EOT, $this->getLogo(), $this->getName(), $this->getVersion());
    }

    /**
     * 获取配置文件
     *
     * @param string $dir
     * @return string|null
     */
    public static function getConfigFile(string $dir): ?string
    {
        $filePath = "$dir/phpy.json";
        return file_exists($filePath) ? $filePath : null;
    }

    /**
     * 设置配置文件
     *
     * @param string $dir
     * @param array $data
     * @return bool|int
     */
    public static function setConfigFile(string $dir, array $data): bool|int
    {
        $filePath = "$dir/phpy.json";
        if (file_exists($filePath)) {
            return false;
        }
        return file_put_contents($filePath, json_encode($data, JSON_UNESCAPED_UNICODE));
    }

    /**
     * 获取锁定文件
     *
     * @param string $dir
     * @return string|null
     */
    public static function getLockFile(string $dir): ?string
    {
        $filePath = "$dir/phpy.lock";
        return file_exists($filePath) ? $filePath : null;
    }

    /**
     * 设置锁定文件
     *
     * @param string $dir
     * @param array $data
     * @return bool|int
     */
    public static function setLockFile(string $dir, array $data): bool|int
    {
        $filePath = "$dir/phpy.lock";
        if (file_exists($filePath) or !isset($data['hash'])) {
            return false;
        }
        return file_put_contents($filePath, json_encode($data, JSON_UNESCAPED_UNICODE));
    }

    /**
     * 获取锁定文件
     *
     * @param string $dir
     * @return string|null
     */
    public static function getRequirementsFile(string $dir): ?string
    {
        $filePath = "$dir/requirements.txt";
        return file_exists($filePath) ? $filePath : null;
    }

    /**
     * 递归向上查找配置文件
     *
     * @param Closure|null $closure
     * @return string|null
     */
    public static function findConfigFile(?Closure $closure = null): string|null
    {
        $currentDir = $startDir = System::getcwd();
        while ($currentDir !== dirname($currentDir)) {dump(1);
            if ($filePath = static::getConfigFile($currentDir)) {
                return $closure ? call_user_func($closure, $filePath, $currentDir, $startDir) : $filePath;
            }
            $currentDir = dirname($currentDir);
        }
        return null;
    }

    /**
     * 递归向上查找锁定文件
     *
     * @param Closure|null $closure
     * @return string|null
     */
    public static function findLockFile(?Closure $closure = null): ?string
    {
        $currentDir = $startDir = System::getcwd();
        while ($currentDir !== dirname($currentDir)) {
            if ($filePath = static::getLockFile($currentDir)) {
                return $closure ? call_user_func($closure, $filePath, $currentDir, $startDir) : $filePath;
            }
            $currentDir = dirname($currentDir);
        }
        return null;
    }

    /**
     * 递归向上查找requirements.txt文件
     *
     * @param Closure|null $closure
     * @return string|null
     */
    public static function findRequirementsFile(?Closure $closure = null): ?string
    {
        $currentDir = $startDir = System::getcwd();
        while ($currentDir !== dirname($currentDir)) {
            if ($filePath = static::getRequirementsFile($currentDir)) {
                return $closure ? call_user_func($closure, $filePath, $currentDir, $startDir) : $filePath;
            }
            $currentDir = dirname($currentDir);
        }
        return null;
    }

    /**
     * 获取所有配置文件树
     *
     * @param Closure|null $closure = function ($organization, $package, $configFilePath) {}
     * @return array<string, array<string, string>>|null
     */
    public static function getVendorConfigFiles(?Closure $closure = null): ?array
    {
        if (!is_dir($vendorDir = System::getcwd() . DIRECTORY_SEPARATOR . 'vendor')) {
            return null;
        }

        $configFilesTree = [];
        $organizationDirs = array_filter(glob($vendorDir . '/*'), 'is_dir');

        foreach ($organizationDirs as $organizationDir) {
            $organization = basename($organizationDir);
            $packageDirs = array_filter(glob($organizationDir . '/*'), 'is_dir');

            foreach ($packageDirs as $packageDir) {
                $package = basename($packageDir);
                $configFilePath = "$packageDir/phpy.json";

                if (file_exists($configFilePath)) {
                    $configFilesTree[$organization][$package] = $closure ? call_user_func($closure, $organization, $package, $configFilePath) : $configFilePath;
                }
            }
        }

        return $configFilesTree;
    }
}
