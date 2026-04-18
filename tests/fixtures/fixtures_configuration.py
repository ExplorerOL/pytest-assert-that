import pytest
from pytest_assert_that import assert_that

@pytest.fixture(scope='class')
def use_assertpy_assert():
    assert_that.configure(is_native_assert=False)

@pytest.fixture(scope='class')
def use_native_assert():
    assert_that.configure(is_native_assert=True)