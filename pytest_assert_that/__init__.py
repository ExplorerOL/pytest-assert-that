from __future__ import absolute_import


def _rewrite_assertions_in_assertpy():
    """Rewrite assertions by pytest"""
    try:
        import pytest
    except ImportError:
        # pytest is not available, skip assertion rewriting
        print('Module pytest is not available, skipping assertion rewriting!!!')
        return

    # assertpy = importlib.import_module('assertpy')
    _MODULES_TO_REWRITE = {
        'pytest_assert_that.base',
        'pytest_assert_that.collection',
        'pytest_assert_that.contains',
        'pytest_assert_that.date',
        'pytest_assert_that.dict',
        'pytest_assert_that.dynamic',
        'pytest_assert_that.exception',
        'pytest_assert_that.extracting',
        'pytest_assert_that.file',
        'pytest_assert_that.numeric',
        'pytest_assert_that.snapshot',
        'pytest_assert_that.string',
    }
    for module in _MODULES_TO_REWRITE:
        print(f'Rewriting {module}...')
        pytest.register_assert_rewrite(module)


_rewrite_assertions_in_assertpy()


from pytest_assert_that.assert_that import (
    assert_that,
    assert_warn,
    soft_assertions,
    fail,
    soft_fail,
    add_extension,
    remove_extension,
    WarningLoggingAdapter,
    __version__,
)
from pytest_assert_that.file import contents_of
