<?php

use PHPUnit\Framework\TestCase;

class TypeTest extends TestCase
{
    public function testType()
    {
        $type = PyCore::type(1);
        $this->assertTrue($type instanceof PyType);

        $this->assertEquals("<class 'int'>", (string)$type);
    }

    public function testNewType()
    {
        try {
            new PyType();
        } catch (Error $error) {
            $this->assertStringContainsString('private PyType::__construct()', $error->getMessage());
            $success = false;
        }
        $this->assertFalse($success);
    }
}
