<?php

declare(strict_types=1);

/**
 * Run two HTTP requests in one PHP built-in server process. The server keeps
 * the Python interpreter alive while PHP still performs RINIT/RSHUTDOWN for
 * every request.
 */

function fail(string $message): never
{
    throw new RuntimeException($message);
}

set_exception_handler(static function (Throwable $error): never {
    fwrite(STDERR, "Server lifecycle test failed: {$error->getMessage()}\n");
    exit(1);
});

function request(string $url): array
{
    $context = stream_context_create([
        'http' => [
            'ignore_errors' => true,
            'timeout' => 10,
        ],
    ]);
    $response = file_get_contents($url, false, $context);
    if ($response === false) {
        fail("HTTP request failed: $url");
    }
    try {
        return json_decode($response, true, flags: JSON_THROW_ON_ERROR);
    } catch (JsonException $error) {
        fail("invalid JSON response: $response ({$error->getMessage()})");
    }
}

$root = dirname(__DIR__, 2);
$extension = $argv[1] ?? $root . '/modules/phpy.so';
if (!is_file($extension)) {
    fail("phpy extension not found: $extension");
}

$reservation = stream_socket_server('tcp://127.0.0.1:0', $errorCode, $errorMessage);
if ($reservation === false) {
    fail("unable to reserve an HTTP port: $errorMessage ($errorCode)");
}
$address = stream_socket_get_name($reservation, false);
fclose($reservation);

$temporary = sys_get_temp_dir() . '/phpy-server-' . getmypid();
if (!mkdir($temporary, 0700) && !is_dir($temporary)) {
    fail("unable to create $temporary");
}
$log = $temporary . '/php-server.log';
$process = proc_open(
    [PHP_BINARY, '-n', '-d', 'extension=' . realpath($extension), '-S', $address, '-t', __DIR__],
    [['pipe', 'r'], ['file', $log, 'a'], ['file', $log, 'a']],
    $pipes,
    $root,
);
if (!is_resource($process)) {
    fail('unable to start the PHP built-in server');
}
fclose($pipes[0]);

try {
    $deadline = microtime(true) + 10;
    do {
        $connection = @stream_socket_client('tcp://' . $address, $errorCode, $errorMessage, 0.1);
        if ($connection !== false) {
            fclose($connection);
            break;
        }
        usleep(10_000);
    } while (microtime(true) < $deadline);

    if ($connection === false) {
        fail('PHP server did not start: ' . (file_get_contents($log) ?: ''));
    }

    $baseUrl = 'http://' . $address . '/lifecycle.php?phase=';
    $first = request($baseUrl . 'retain');
    $second = request($baseUrl . 'release');

    if (($first['pid'] ?? null) !== ($second['pid'] ?? null)) {
        fail('requests were not handled by the same server process');
    }
    if (($first['arrayValue'] ?? null) !== 'request value'
        || ($second['released'] ?? null) !== 6
        || ($second['fresh'] ?? null) !== 3
        || !array_key_exists('expiredArrayValue', $second)
        || $second['expiredArrayValue'] !== null) {
        fail('unexpected lifecycle response: ' . json_encode([$first, $second]));
    }
    echo "Cross-request lifecycle test passed (server {$first['pid']})\n";
} finally {
    // SIGINT (2, not the SIGTERM default): the built-in server exits
    // gracefully, running PHP shutdown and flushing gcov data, so the
    // request-shutdown dtor cleanup (phpy's crash-prevention for Python
    // objects that outlive the PHP request) is reflected in the report.
    proc_terminate($process, 2);
    proc_close($process);
    @unlink($log);
    @rmdir($temporary);
}
