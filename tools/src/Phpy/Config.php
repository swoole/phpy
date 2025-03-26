<?php

declare(strict_types=1);

namespace PhpyTool\Phpy;

use PhpyTool\Phpy\Helpers\System;

class Config
{

    /**
     * @var array
     */
    protected array $config = [
        'config' => [
            'cache-dir'     => '~/.cache/phpy',
            'scan-dirs'     => [],
            'pip-index-url' => ''
        ],
        'python' => [
            'source-url'        => 'https://github.com/python/cpython.git',
            'install-dir'       => '/usr',
            'install-version'   => 'v3.13.2',
            'install-configure' => [
                '--enable-shared',
                '--with-system-expat',
                '--with-system-ffi',
                '--enable-ipv6',
                '--enable-loadable-sqlite-extensions',
                '--with-computed-gotos',
                '--with-ensurepip=install',
            ],
        ],
        'phpy' => [
            'source-url'        => 'https://github.com/swoole/phpy.git',
            'install-version'   => 'latest',
            'install-configure' => [],
            'ini-path'          => '/usr/local/etc/php/conf.d/xx-php-ext-phpy.ini'
        ],
        'modules' => []
    ];

    /**
     * @return string
     */
    public function __toString(): string
    {
        $this->config['modules'] = $this->config['modules'] ?: new \stdClass();
        return json_encode($this->config, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT|JSON_UNESCAPED_SLASHES);
    }

    /**
     * @param string|null $file
     */
    public function __construct(?string $file = null)
    {
        if ($file) {
            $this->load($file);
        }
    }

    /**
     * @param string $file
     * @return void
     */
    public function load(string $file): void
    {
        try {
            $config = json_decode(System::getFileContent($file), true, flags: JSON_THROW_ON_ERROR);
        } catch (\Throwable) {}
        $this->config = array_replace_recursive($this->config, $config ?? []);
    }

    /**
     * 获取配置
     *
     * @param string|null $key
     * @param mixed|null $default
     * @return mixed
     */
    public function get(?string $key, mixed $default = null): mixed
    {
        $config = $this->config;
        if ($key) {
            $keyArray = explode('.', $key);
            $found = true;
            foreach ($keyArray as $index) {
                if (!isset($config[$index])) {
                    $found = false;
                    break;
                }
                $config = $config[$index];
            }

            return $found ? $config : $default;
        }

        return $config;
    }

    /**
     * @param string $key
     * @param mixed $value
     * @return void
     */
    public function set(string $key, mixed $value): void
    {
        $keys = explode('.', $key);
        $config = &$this->config;

        foreach ($keys as $k) {
            if (!isset($config[$k]) or !is_array($config[$k])) {
                $config[$k] = [];
            }
            $config = &$config[$k];
        }

        $config = $value;
    }

    /**
     * @return array
     */
    public function all(): array
    {
        $this->config['modules'] = $this->config['modules'] ?: new \stdClass();
        return $this->config;
    }
}
