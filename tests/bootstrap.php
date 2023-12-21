<?php

declare(strict_types=1);

ini_set('display_errors', 'on');
ini_set('display_startup_errors', 'on');

error_reporting(E_ALL & ~E_DEPRECATED);
date_default_timezone_set('Asia/Shanghai');

!defined('BASE_PATH') && define('BASE_PATH', dirname(__DIR__, 1));

require BASE_PATH . '/vendor/autoload.php';

PyCore::import('sys')->path->append(__DIR__ . '/lib');

class PyLoader
{
    static array $modules;

    static function import(string $name)
    {
        if (!isset(self::$modules[$name])) {
            self::$modules[$name] = PyCore::import($name);
        }
        return self::$modules[$name];
    }
}


class FnCallableClass
{
    private $phpunit;
    private $uuid;

    function __construct($phpunit, $uuid)
    {
        $this->phpunit = $phpunit;
        $this->uuid = $uuid;
    }

    function __invoke($namespace)
    {
        $this->phpunit->assertEquals($namespace, 'app.user');
        return $this->uuid;
    }

    function test($namespace)
    {
        $this->phpunit->assertEquals($namespace, 'app.user');
        return $this->uuid;
    }
}

