<?php


use PHPUnit\Framework\TestCase;

class DictTest extends TestCase
{
    public function testDict()
    {
        $dict = new PyDict;
        $dict['hello'] = uniqid();

        $this->assertTrue(isset($dict['hello']));
        $this->assertFalse(isset($dict['golang']));

        unset($dict['hello']);
        $this->assertFalse(isset($dict['hello']));

        $n = 10;
        while ($n--) {
            $dict['key-' . $n] = uniqid();
        }

        $this->assertEquals(10, $dict->count());
    }
}
