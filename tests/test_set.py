import pytest
import phpy
import os


def test_set():
    s = {1, 3, 5, 2023, 7, 9}
    if os.environ.get('IN_CI'):
        assert phpy.call('array_search', 2023, s) == 4
    else:
        assert phpy.call('array_search', 2023, s) == 2
