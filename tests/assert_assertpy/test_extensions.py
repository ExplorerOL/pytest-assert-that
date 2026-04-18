# Copyright (c) 2015-2019, Activision Publishing, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import numbers

import pytest
from pytest_assert_that import assert_that, add_extension, remove_extension, fail


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


def dupe1():
    add_extension(is_foo)
    assert_that('foo').is_foo()
    try:
        assert_that('FOO').is_foo()
        fail('should have raised error')
    except AssertionError as ex:
        assert_that(str(ex)).is_equal_to('Expected <FOO> to be foo, but was not.')



def dupe2():
    def is_foo(myself):
        if myself.val != 'FOO':
            return myself.error('Expected <%s> to be FOO, but was not.' % (myself.val))
        return myself

    add_extension(is_foo)
    assert_that('FOO').is_foo()
    try:
        assert_that('foo').is_foo()
        fail('should have raised error')
    except AssertionError as ex:
        assert_that(str(ex)).is_equal_to('Expected <foo> to be FOO, but was not.')


add_extension(is_even)
add_extension(is_multiple_of)
add_extension(is_factor_of)

@pytest.mark.usefixtures("use_assertpy_assert")
class TestExtensionsAssertpyAssertions:
    def test_is_even_extension(self):
        assert_that(124).is_even()
        assert_that(124).is_type_of(int).is_even().is_greater_than(123).is_less_than(125).is_equal_to(124)


    def test_is_even_extension_failure(self):
        try:
            assert_that(123).is_even()
            fail('should have raised error')
        except AssertionError as ex:
            assert_that(str(ex)).is_equal_to('Expected <123> to be even, but was not.')


    def test_is_even_extension_failure_not_callable(self):
        try:
            add_extension('foo')
            fail('should have raised error')
        except TypeError as ex:
            assert_that(str(ex)).is_equal_to('func must be callable')


    def test_is_even_extension_failure_not_integer(self):
        try:
            assert_that(124.0).is_even()
            fail('should have raised error')
        except TypeError as ex:
            assert_that(str(ex)).is_equal_to('val must be an integer')


    def test_is_multiple_of_extension(self):
        assert_that(24).is_multiple_of(1)
        assert_that(24).is_multiple_of(2)
        assert_that(24).is_multiple_of(3)
        assert_that(24).is_multiple_of(4)
        assert_that(24).is_multiple_of(6)
        assert_that(24).is_multiple_of(8)
        assert_that(24).is_multiple_of(12)
        assert_that(24).is_multiple_of(24)
        assert_that(124).is_type_of(int).is_even().is_multiple_of(31).is_equal_to(124)


    def test_is_multiple_of_extension_failure(self):
        try:
            assert_that(24).is_multiple_of(5)
            fail('should have raised error')
        except AssertionError as ex:
            assert_that(str(ex)).is_equal_to('Expected <24> to be multiple of <5>, but was not.')


    def test_is_multiple_of_extension_failure_bad_val(self):
        try:
            assert_that(24.0).is_multiple_of(5)
            fail('should have raised error')
        except TypeError as ex:
            assert_that(str(ex)).is_equal_to('val must be a positive integer')


    def test_is_multiple_of_extension_failure_negative_val(self):
        try:
            assert_that(-24).is_multiple_of(6)
            fail('should have raised error')
        except TypeError as ex:
            assert_that(str(ex)).is_equal_to('val must be a positive integer')


    def test_is_multiple_of_extension_failure_bad_arg(self):
        try:
            assert_that(24).is_multiple_of('foo')
            fail('should have raised error')
        except TypeError as ex:
            assert_that(str(ex)).is_equal_to('given arg must be a positive integer')


    def test_is_multiple_of_extension_failure_negative_arg(self):
        try:
            assert_that(24).is_multiple_of(-6)
            fail('should have raised error')
        except TypeError as ex:
            assert_that(str(ex)).is_equal_to('given arg must be a positive integer')


    def test_is_factor_of_extension(self):
        assert_that(1).is_factor_of(24)
        assert_that(2).is_factor_of(24)
        assert_that(3).is_factor_of(24)
        assert_that(4).is_factor_of(24)
        assert_that(6).is_factor_of(24)
        assert_that(8).is_factor_of(24)
        assert_that(12).is_factor_of(24)
        assert_that(24).is_factor_of(24)
        assert_that(31).is_type_of(int).is_factor_of(124).is_equal_to(31)


    def test_is_factor_of_extension_failure(self):
        try:
            assert_that(5).is_factor_of(24)
            fail('should have raised error')
        except AssertionError as ex:
            assert_that(str(ex)).is_equal_to('Expected <5> to be factor of <24>, but was not.')


    def test_call_missing_extension(self):
        def is_missing(): pass
        try:
            remove_extension(is_even)
            remove_extension(is_multiple_of)
            remove_extension(is_factor_of)
            remove_extension(is_missing)
            assert_that(24).is_multiple_of(6)
            fail('should have raised error')
        except AttributeError as ex:
            assert_that(str(ex)).is_equal_to('pytest-assert-that has no assertion <is_multiple_of()>')


    def test_remove_bad_extension(self):
        try:
            remove_extension('foo')
            fail('should have raised error')
        except TypeError as ex:
            assert_that(str(ex)).is_equal_to('func must be callable')



    def test_dupe_extensions(self):
        dupe1()
        dupe2()
        dupe1()
