<?php

namespace phpunit;

use PHPUnit\Framework\TestCase;
use PyCore;

class LocaleTest extends TestCase
{
    public function testLocale()
    {
        $fileName = __DIR__ . '/test_locale.py';
        file_put_contents($fileName, <<<PYCODE
        import locale;
        import sys;

        print(locale.getdefaultlocale())
        print(locale.getpreferredencoding())
        print(sys.getdefaultencoding())
        print(sys.getfilesystemencoding())
        PYCODE);

        $result = shell_exec('python ' . $fileName);
        unlink($fileName);

        $locale = PyCore::import('locale');
        $sys = PyCore::import('sys');
        $this->assertEquals(sprintf("%s\n%s\n%s\n%s\n", $locale->getdefaultlocale(), $locale->getpreferredencoding(), $sys->getdefaultencoding(), $sys->getfilesystemencoding()), $result);
    }
}
