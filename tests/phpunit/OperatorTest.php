<?php


namespace phpunit;

use PHPUnit\Framework\TestCase;
use PyCore;
use PyStr;

class OperatorTest extends TestCase
{
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
        $arr /= 5;
        $this->assertArrayValues($arr, 7, 12);
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
        $this->assertTrue(PyCore::scalar($s) == "hello world");

        $s .= "\n";
        $this->assertTrue(PyCore::scalar($s) == "hello world");
    }
}
