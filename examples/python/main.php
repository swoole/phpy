<?php
function main()
{
    $set = new PyList();
    $v1 = random_int(1000, 99999);
    $v2 = random_int(1000, 99999);

    $set[] = 2;
    $set[] = $v1;
    $set[] = $v2;
    $set[] = 12345;

    $set[3] = 9999;

    var_dump($set[3]);
}

function test2()
{

    $userType = $m->User;
    $u = $userType('rango');
    var_dump($userType);
    var_dump($u);
    //    $u = $m->User('rango');
//    $n = 5;
//    while ($n--) {
//        $u->kwargs('xd', 'jd', date: date('Y-m-d'));
//    }
}

function test3()
{
    $i = PyCore::int(12345435);

    var_dump(strval($i->__pow__(3)));
}

function test4()
{
    $fn = PyCore::fn(function ($o) {
        var_dump($o);
    });

    var_dump($fn);

    $fn('hello');
}

function test5()
{
    $m = PyCore::import('app.user');
    $uuid = uniqid();
    var_dump($uuid);
    $rs = $m->test_callback(PyCore::fn(function ($namespace) use ($uuid) {
        var_dump($namespace);
        return $uuid;
    }));
    var_dump($rs);
}

function test6()
{
    $m = PyCore::import('app.user');
    $list = $m->lazy_square(5);
    $iter = PyCore::iter($list);

    while ($next = PyCore::next($iter)) {
        var_dump(PyCore::scalar($next));
    }
}

function test7()
{
    $sys = PyCore::import('sys');
    $os = PyCore::import('os');
    $uname = $os->uname();

    $iter = PyCore::iter($uname);
    var_dump($iter instanceof PyIter);

    while ($next = PyCore::next($iter)) {
        var_dump(PyCore::scalar($next));
    }
}


class Test {
    static function test() {
        var_dump(__METHOD__);
    }
}
