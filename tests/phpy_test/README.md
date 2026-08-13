# phpy_test

`phpy_test` is phpy's internal test extension, analogous to PHP's `zend_test`
extension. It exposes selected internal C and C++ paths that cannot be reached
through phpy's public PHP API, so those paths can be covered by PHPUnit.

The extension is test-only. It must not be installed or distributed as part of
the phpy runtime package, and its PHP functions are not public API.
