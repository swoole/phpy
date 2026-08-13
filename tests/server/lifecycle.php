<?php

declare(strict_types=1);

header('Content-Type: application/json');

$module = PyCore::import('sys');
$module->path->append(__DIR__);
$store = PyCore::import('lifecycle_store');
$phase = $_GET['phase'] ?? '';

if ($phase === 'retain') {
    $stream = fopen('php://temp', 'w+');
    $types = $store->retain(
        new PyObject(['key' => 'value']),
        new PyObject('request-owned string'),
        new PyObject(static fn(int $value): int => $value + 1),
        new PyObject((object) ['value' => 42]),
        new PyObject($stream),
    )->toArray();

    $arrayValue = PyCore::scalar($store->create_request_array());
    echo json_encode([
        'phase' => 'retain',
        'pid' => getmypid(),
        'types' => $types,
        'arrayValue' => $arrayValue,
    ], JSON_THROW_ON_ERROR);
    return;
}

if ($phase === 'release') {
    $expiredArrayValue = $store->read_expired_array();
    $released = $store->release();
    $fresh = PyCore::import('builtins')->len([1, 2, 3]);

    echo json_encode([
        'phase' => 'release',
        'pid' => getmypid(),
        'released' => $released,
        'fresh' => $fresh,
        'expiredArrayValue' => $expiredArrayValue,
    ], JSON_THROW_ON_ERROR);
    return;
}

http_response_code(400);
echo json_encode(['error' => 'unknown phase'], JSON_THROW_ON_ERROR);
