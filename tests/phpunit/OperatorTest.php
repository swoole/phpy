<?php


namespace phpunit;

use PHPUnit\Framework\TestCase;
use PyCore;
use PyStr;

class OperatorTest extends TestCase
{
    protected function setUp(): void
    {
        PyCore::setOptions(['return_as_object' => true]);
    }

    protected function tearDown(): void
    {
        PyCore::setOptions(['return_as_object' => false]);
    }

    private function assertArrayValues($arr, $v0, $v1): void
    {
        $this->assertTrue($arr[0] == $v0);
        $this->assertTrue($arr[1] == $v1);
    }

    public function testNumberOperator()
    {
        $np = PyCore::import('numpy');
        $arr = $np->array([3, 4]);
        $this->assertArrayValues($arr, 3, 4);

        $arr2 = $arr * 3;
        $this->assertArrayValues($arr2, 9, 12);

        $arr3 = $arr2 + 5;
        $this->assertArrayValues($arr3, 14, 17);

        $arr4 = $arr3 - 5;
        $this->assertArrayValues($arr4, 9, 12);

        $arr5 = $arr4 / 3;
        $this->assertArrayValues($arr5, 3, 4);

        $arr6 = $arr5 ** 2;
        $this->assertArrayValues($arr6, 9, 16);

        $arr7 = $arr6 % 5;
        $this->assertArrayValues($arr7, 4, 1);
    }

    public function testUnaryOperator()
    {
        $np = PyCore::import('numpy');
        $arr = $np->array([7, 12]);
        $this->assertArrayValues($arr, 7, 12);

        $arr2 = -$arr;
        $this->assertArrayValues($arr2, -7, -12);
    }

    public function testBitwiseOperator()
    {
        $np = PyCore::import('numpy');
        $arr = $np->array([7, 12]);
        $this->assertArrayValues($arr, 7, 12);
        $arr2 = $arr & 3;
        $this->assertArrayValues($arr2, 3, 0);
        $arr3 = $arr | 3;
        $this->assertArrayValues($arr3, 7, 15);
        $arr4 = $arr ^ 3;
        $this->assertArrayValues($arr4, 4, 15);
        $arr5 = $arr << 2;
        $this->assertArrayValues($arr5, 28, 48);
        $arr6 = $arr >> 2;
        $this->assertArrayValues($arr6, 1, 3);
        $arr7 = ~$arr;
        $this->assertArrayValues($arr7, -8, -13);
    }

    public function testAssignmentOperator()
    {
        $np = PyCore::import('numpy');
        $arr = $np->array([7, 12]);
        $this->assertArrayValues($arr, 7, 12);
        $arr += 5;
        $this->assertArrayValues($arr, 12, 17);
        $arr -= 5;
        $this->assertArrayValues($arr, 7, 12);
        $arr *= 5;
        $this->assertArrayValues($arr, 35, 60);

        $div = $np->array([7.0, 12.0]);
        $div /= 5;
        $this->assertArrayValues($div, 1.4, 2.4);

        $arr = $np->array([7, 12]);
        $arr **= 3;
        $this->assertArrayValues($arr, 343, 1728);
        $arr %= 17;
        $this->assertArrayValues($arr, 3, 11);
        $arr &= 3;
        $this->assertArrayValues($arr, 3, 3);

        $arr2 = $np->array([7, 12]);
        $arr2 <<= 4;
        $this->assertArrayValues($arr2, 112, 192);
        $arr2 >>= 3;
        $this->assertArrayValues($arr2, 14, 24);
        $arr2 ^= 3;
        $this->assertArrayValues($arr2, 13, 27);
        $arr2 |= 9;
        $this->assertArrayValues($arr2, 13, 27);
    }

    public function testComparisonOperator()
    {
        $v = PyCore::int(1999);
        $this->assertTrue($v == 1999);
        $this->assertFalse($v == 2000);
        $this->assertFalse($v != 1999);
        $this->assertTrue($v != 2000);

        $this->assertFalse($v > 1999);
        $this->assertTrue($v > 1000);

        $this->assertFalse($v < 1000);
        $this->assertTrue($v < 3000);

        $this->assertTrue($v >= 1999);
        $this->assertFalse($v >= 3000);
        $this->assertTrue($v <= 1999);
        $this->assertFalse($v <= 1000);
    }

    public function testException()
    {
        $s = PyCore::str("hello world");
        $s += "\n";
        $this->assertSame("hello world\n", PyCore::scalar($s));

        $s .= "\n";
        $this->assertSame("hello world\n", PyCore::scalar($s));
    }

    public function testDivisionUsesPythonTrueDivision(): void
    {
        $value = PyCore::int(7);
        $result = $value / 2;

        $this->assertSame(3.5, PyCore::scalar($result));
    }

    public function testCompoundAssignmentReplacesImmutablePythonValue(): void
    {
        $value = PyCore::int(5);
        $value += 2;

        $this->assertSame(7, PyCore::scalar($value));
    }

    public function testCompoundAssignmentPreservesZendReferencesAndExpressionResult(): void
    {
        $value = PyCore::int(5);
        $reference =& $value;
        $result = ($reference += 2);

        $this->assertSame(7, PyCore::scalar($value));
        $this->assertSame(7, PyCore::scalar($reference));
        $this->assertSame(7, PyCore::scalar($result));
    }

    public function testFailedCompoundAssignmentKeepsOriginalValue(): void
    {
        $value = PyCore::int(7);

        try {
            $value /= 0;
            $this->fail('Division by zero must fail');
        } catch (\PyError $error) {
            $this->assertStringContainsString('division by zero', $error->getMessage());
        }

        $this->assertSame(7, PyCore::scalar($value));
    }

    public function testCompoundAssignmentDoesNotLeakInPlaceResultReference(): void
    {
        $sys = PyCore::import('sys');
        $value = PyCore::list([]);
        $before = PyCore::scalar($sys->getrefcount($value));

        for ($i = 0; $i < 100; $i++) {
            $value += [];
        }

        $this->assertSame($before, PyCore::scalar($sys->getrefcount($value)));
    }

    public function testOperatorErrorsAreConvertedToPyError(): void
    {
        try {
            $result = PyCore::int(1) / 0;
            $this->fail('Division by zero must fail');
        } catch (\PyError $error) {
            $this->assertStringContainsString('division by zero', $error->getMessage());
        }

        try {
            $result = ~PyCore::str('not-an-integer');
            $this->fail('Unsupported invert must fail');
        } catch (\PyError $error) {
            $this->assertStringContainsString('bad operand type', $error->getMessage());
        }
    }

    public function testIdentityUsesPythonObjectIdentity(): void
    {
        $first = PyCore::import('sys');
        $second = PyCore::import('sys');
        $equalButDistinct = PyCore::list([]);

        $this->assertTrue($first === $second);
        $this->assertFalse($first !== $second);
        $this->assertFalse($first === $equalButDistinct);
        $this->assertTrue($first !== $equalButDistinct);
    }

    public function testTruthinessUsesPythonBoolProtocol(): void
    {
        $class = PyCore::import('app.user')->OperatorProtocol;
        $falsey = $class(false);
        $truthy = $class(true);

        $this->assertTrue(!$falsey);
        $this->assertFalse((bool) $falsey);
        $this->assertFalse(!$truthy);
        $this->assertTrue((bool) $truthy);

        $entered = false;
        if ($falsey) {
            $entered = true;
        }
        $this->assertFalse($entered);
    }

    public function testReflectedProtocolMatchesPython(): void
    {
        $value = PyCore::import('app.user')->OperatorProtocol(false);

        $this->assertSame('rsub:10', PyCore::scalar(10 - $value));
    }

    public function testOperatorNoneResultRemainsWrappedWhenRequested(): void
    {
        $value = PyCore::import('app.user')->OperatorProtocol(false);
        $result = $value + 1;

        $this->assertInstanceOf(\PyObject::class, $result);
        $this->assertNull(PyCore::scalar($result));
    }
}
