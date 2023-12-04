<?php


use PHPUnit\Framework\TestCase;

class ObjectTest extends TestCase
{
    protected function assertForKwargs($inst) {
        $today = date('Y-m-d');
        $this->assertEquals(strval($inst->args['a']), 'a');
        $this->assertEquals(strval($inst->args['name']), 'default_name');
        $this->assertEquals(strval($inst->args['date']), $today);
    }
    public function testKwargs()
    {
        $user = PyCore::import('app.user');
        $class = $user->KwargsCtor;
        // __invoke
        $inst = $class('a', 'b', date: date('Y-m-d'));
        $this->assertForKwargs($inst);
        // __call
        $inst = $user->KwargsCtor('a', 'b', date: date('Y-m-d'));
        $this->assertForKwargs($inst);
    }
}
