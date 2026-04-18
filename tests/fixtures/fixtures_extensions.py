import numbers

import pytest
from pytest_assert_that import assert_that, add_extension

def is_even(myself):
    if isinstance(myself.val, numbers.Integral) is False:
        raise TypeError('val must be an integer')
    if myself.val % 2 != 0:
        return myself.error('Expected <%s> to be even, but was not.' % (myself.val))
    return myself


def is_multiple_of(myself, other):
    if isinstance(myself.val, numbers.Integral) is False or myself.val <= 0:
        raise TypeError('val must be a positive integer')

    if isinstance(other, numbers.Integral) is False or other <= 0:
        raise TypeError('given arg must be a positive integer')

    _, rem = divmod(myself.val, other)
    if rem > 0:
        return myself.error('Expected <%s> to be multiple of <%s>, but was not.' % (myself.val, other))

    return myself


def is_factor_of(myself, other):
    if isinstance(myself.val, numbers.Integral) is False or myself.val <= 0:
        raise TypeError('val must be a positive integer')

    if isinstance(other, numbers.Integral) is False or other <= 0:
        raise TypeError('given arg must be a positive integer')

    _, rem = divmod(other, myself.val)
    if rem > 0:
        return myself.error('Expected <%s> to be factor of <%s>, but was not.' % (myself.val, other))

    return myself


def is_foo(myself):
    if myself.val != 'foo':
        return myself.error('Expected <%s> to be foo, but was not.' % (myself.val))
    return myself

@pytest.fixture
def add_custom_extensions():
    add_extension(is_even)
    add_extension(is_multiple_of)
    add_extension(is_factor_of)
