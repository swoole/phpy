<?php

declare(strict_types=1);

/**
 * Run two requests in one PHP-FPM worker to verify that Python objects may
 * outlive request-owned Zend values without a double destructor or UAF.
 */

function fail(string $message): never
{
    throw new RuntimeException($message);
}

set_exception_handler(static function (Throwable $error): never {
    fwrite(STDERR, "FPM lifecycle test failed: {$error->getMessage()}\n");
    exit(1);
});

function findExecutable(array $candidates): ?string
{
    foreach ($candidates as $candidate) {
        if ($candidate !== '' && is_executable($candidate)) {
            return $candidate;
        }
    }
    return null;
}

function request(string $client, string $socket, string $script, string $phase): array
{
    $environment = array_merge(getenv(), [
        'GATEWAY_INTERFACE' => 'CGI/1.1',
        'REQUEST_METHOD' => 'GET',
        'SCRIPT_FILENAME' => $script,
        'SCRIPT_NAME' => '/lifecycle.php',
        'REQUEST_URI' => '/lifecycle.php?phase=' . $phase,
        'QUERY_STRING' => 'phase=' . $phase,
        'SERVER_PROTOCOL' => 'HTTP/1.1',
        'SERVER_NAME' => 'localhost',
        'SERVER_PORT' => '80',
        'REMOTE_ADDR' => '127.0.0.1',
    ]);
    $pipes = [];
    $process = proc_open(
        [$client, '-bind', '-connect', $socket],
        [['pipe', 'r'], ['pipe', 'w'], ['pipe', 'w']],
        $pipes,
        null,
        $environment,
    );
    if (!is_resource($process)) {
        fail('unable to start cgi-fcgi');
    }
    fclose($pipes[0]);
    $stdout = stream_get_contents($pipes[1]);
    $stderr = stream_get_contents($pipes[2]);
    fclose($pipes[1]);
    fclose($pipes[2]);
    $status = proc_close($process);
    if ($status !== 0) {
        fail("cgi-fcgi exited with $status: $stderr");
    }

    $parts = preg_split("/\r?\n\r?\n/", $stdout, 2);
    if (count($parts) !== 2) {
        fail("invalid FastCGI response: $stdout");
    }
    try {
        return json_decode(trim($parts[1]), true, flags: JSON_THROW_ON_ERROR);
    } catch (JsonException $error) {
        fail("invalid JSON response: {$parts[1]} ({$error->getMessage()})");
    }
}

$root = dirname(__DIR__, 2);
$extension = $argv[1] ?? $root . '/modules/phpy.so';
if (!is_file($extension)) {
    fail("phpy extension not found: $extension");
}

$version = PHP_MAJOR_VERSION . '.' . PHP_MINOR_VERSION;
$fpm = findExecutable(array_filter([
    getenv('PHP_FPM_BINARY') ?: '',
    '/usr/sbin/php-fpm' . $version,
    '/usr/local/sbin/php-fpm',
]));
$client = findExecutable(array_filter([
    getenv('CGI_FCGI_BINARY') ?: '',
    '/usr/bin/cgi-fcgi',
]));
if ($fpm === null || $client === null) {
    fail('php-fpm and cgi-fcgi are required');
}

$temporary = sys_get_temp_dir() . '/phpy-fpm-' . getmypid();
if (!mkdir($temporary, 0700) && !is_dir($temporary)) {
    fail("unable to create $temporary");
}
$socket = $temporary . '/php-fpm.sock';
$configuration = $temporary . '/php-fpm.conf';
$log = $temporary . '/php-fpm.log';
$user = function_exists('posix_getpwuid') ? posix_getpwuid(posix_geteuid())['name'] : get_current_user();
$group = function_exists('posix_getgrgid') ? posix_getgrgid(posix_getegid())['name'] : $user;
$config = <<<CONF
[global]
daemonize = no
error_log = $log

[www]
listen = $socket
listen.owner = $user
listen.group = $group
user = $user
group = $group
pm = static
pm.max_children = 1
clear_env = no
catch_workers_output = yes
php_admin_value[display_errors] = 1
php_admin_value[log_errors] = 1
CONF;
file_put_contents($configuration, $config);

$pipes = [];
$command = [$fpm, '-F', '-y', $configuration, '-d', 'extension=' . realpath($extension)];
if (function_exists('posix_geteuid') && posix_geteuid() === 0) {
    $command[] = '-R';
}
$process = proc_open(
    $command,
    [['pipe', 'r'], ['file', $log, 'a'], ['file', $log, 'a']],
    $pipes,
    $root,
);
if (!is_resource($process)) {
    fail('unable to start php-fpm');
}
fclose($pipes[0]);

try {
    $deadline = microtime(true) + 10;
    while (!file_exists($socket) && microtime(true) < $deadline) {
        usleep(10_000);
    }
    if (!file_exists($socket)) {
        fail('php-fpm did not create its socket: ' . (file_get_contents($log) ?: ''));
    }

    $first = request($client, $socket, __DIR__ . '/lifecycle.php', 'retain');
    $second = request($client, $socket, __DIR__ . '/lifecycle.php', 'release');

    if (($first['pid'] ?? null) !== ($second['pid'] ?? null)) {
        fail('requests were not handled by the same worker');
    }
    if (($first['arrayValue'] ?? null) !== 'request value'
        || ($second['released'] ?? null) !== 5
        || ($second['fresh'] ?? null) !== 3
        || !array_key_exists('expiredArrayValue', $second)
        || $second['expiredArrayValue'] !== null) {
        fail('unexpected lifecycle response: ' . json_encode([$first, $second]));
    }
    echo "PHP-FPM cross-request lifecycle test passed (worker {$first['pid']})\n";
} finally {
    proc_terminate($process);
    proc_close($process);
    @unlink($socket);
    @unlink($configuration);
    @unlink($log);
    @rmdir($temporary);
}
