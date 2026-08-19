<?php

namespace phpunit;

use PHPUnit\Framework\TestCase;

final class OperatorConfigurationTest extends TestCase
{
    public function testOperatorOverloadingIsEnabledByDefault(): void
    {
        $script = <<<'PHP'
if (ini_get('phpy.enable_operator_overloading') !== '1') {
    fwrite(STDERR, "operator option is not enabled by default\n");
    exit(1);
}

$value = PyCore::int(20);
if (PyCore::scalar($value + 22) !== 42) {
    fwrite(STDERR, "operator overloading is inactive\n");
    exit(2);
}
echo "enabled\n";
PHP;

        $this->assertSame("enabled\n", $this->runWithLocalExtension($script));
    }

    public function testOperatorOverloadingCanBeDisabledBeforeModuleStartup(): void
    {
        $script = <<<'PHP'
if (ini_get('phpy.enable_operator_overloading') !== '0') {
    fwrite(STDERR, "operator option was not disabled\n");
    exit(1);
}

$value = PyCore::int(42);
if (PyCore::scalar($value) !== 42) {
    fwrite(STDERR, "ordinary phpy calls stopped working\n");
    exit(2);
}

try {
    $unused = $value + 1;
    fwrite(STDERR, "operator overloading remained enabled\n");
    exit(3);
} catch (TypeError $error) {
    echo "disabled\n";
}
PHP;
        $this->assertSame(
            "disabled\n",
            $this->runWithLocalExtension($script, 'phpy.enable_operator_overloading=0'),
        );
    }

    public function testOperatorOptionCannotChangeAtRequestTime(): void
    {
        $script = <<<'PHP'
if (ini_set('phpy.enable_operator_overloading', '0') !== false) {
    fwrite(STDERR, "system option changed at request time\n");
    exit(1);
}
if (ini_get('phpy.enable_operator_overloading') !== '1') {
    fwrite(STDERR, "system option value changed at request time\n");
    exit(2);
}
echo "immutable\n";
PHP;

        $this->assertSame("immutable\n", $this->runWithLocalExtension($script));
    }

    private function runWithLocalExtension(string $script, ?string $option = null): string
    {
        $extension = dirname(__DIR__, 2) . '/modules/phpy.' . PHP_SHLIB_SUFFIX;
        if (!is_file($extension)) {
            $this->markTestSkipped('The locally built phpy extension is unavailable');
        }

        $command = [PHP_BINARY, '-n', '-d', 'extension=' . $extension];
        if ($option !== null) {
            array_push($command, '-d', $option);
        }
        array_push($command, '-r', $script);

        $pipes = [];
        $process = proc_open($command, [1 => ['pipe', 'w'], 2 => ['pipe', 'w']], $pipes);
        $this->assertIsResource($process);

        $stdout = stream_get_contents($pipes[1]);
        $stderr = stream_get_contents($pipes[2]);
        fclose($pipes[1]);
        fclose($pipes[2]);
        $status = proc_close($process);

        $this->assertSame(0, $status, $stderr);
        return $stdout;
    }
}
