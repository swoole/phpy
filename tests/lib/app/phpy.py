import phpy


def test_import():
    return phpy.call('get_loaded_extensions', False)
