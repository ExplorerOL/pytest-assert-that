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
import re
from dataclasses import dataclass

import abc
import pytest

from pytest_assert_that import assert_that, fail


class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def say_hello(self):
        return 'Hello, %s!' % self.first_name


class Developer(Person):
    def say_hello(self):
        return '%s writes code.' % self.first_name


class AbstractAutomobile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractproperty
    def classification(self):
        raise NotImplementedError('This method must be overridden')


class Car(AbstractAutomobile):
    @property
    def classification(self):
        return 'car'


class Truck(AbstractAutomobile):
    @property
    def classification(self):
        return 'truck'


@dataclass
class PersonDataclass(object):
    first_name: str
    last_name: str
    age: int


fred = Person('Fred', 'Smith')
nick = Person('Nik', 'Smith')
ann = PersonDataclass('Ann', 'Doe', 24)
kate = PersonDataclass('Kate', 'Doe', 35)
joe = Developer('Joe', 'Coder')
people = [fred, joe]
car = Car()
truck = Truck()


@pytest.mark.usefixtures("use_assertpy_assert")
class TestClassAssertpyAssertions:

    def test_is_type_of(self):
        assert_that(fred).is_type_of(Person)
        assert_that(joe).is_type_of(Developer)
        assert_that(car).is_type_of(Car)
        assert_that(truck).is_type_of(Truck)


    def test_is_type_of_class(self):
        assert_that(fred.__class__).is_type_of(Person.__class__)


    def test_is_type_of_class_failure(self):
        try:
            assert_that(fred.__class__).is_type_of(Person)
            fail('should have raised error')
        except AssertionError as ex:
            assert_that(str(ex)).contains('to be of type <Person>, but was not')


    def test_is_instance_of(self):
        assert_that(fred).is_instance_of(Person)
        assert_that(fred).is_instance_of(object)

        assert_that(joe).is_instance_of(Developer)
        assert_that(joe).is_instance_of(Person)
        assert_that(joe).is_instance_of(object)

        assert_that(car).is_instance_of(Car)
        assert_that(car).is_instance_of(AbstractAutomobile)
        assert_that(car).is_instance_of(object)

        assert_that(truck).is_instance_of(Truck)
        assert_that(truck).is_instance_of(AbstractAutomobile)
        assert_that(truck).is_instance_of(object)


    def test_is_instance_of_class(self):
        assert_that(fred.__class__).is_instance_of(Person.__class__)


    def test_is_instance_of_class_failure(self):
        try:
            assert_that(fred.__class__).is_instance_of(Person)
            fail('should have raised error')
        except AssertionError as ex:
            assert_that(str(ex)).contains('to be instance of class <Person>, but was not')


    def test_extract_attribute(self):
        assert_that(people).extracting('first_name').is_equal_to(['Fred', 'Joe'])
        assert_that(people).extracting('first_name').contains('Fred', 'Joe')


    def test_extract_property(self):
        assert_that(people).extracting('name').contains('Fred Smith', 'Joe Coder')


    def test_extract_multiple(self):
        assert_that(people).extracting('first_name', 'name').contains(
            ('Fred', 'Fred Smith'), ('Joe', 'Joe Coder')
        )


    def test_extract_zero_arg_method(self):
        assert_that(people).extracting('say_hello').contains('Hello, Fred!', 'Joe writes code.')


    def test_class_is_equal_to(self):
        assert_that(fred).is_equal_to(fred)


    def test_dataclass_is_equal_to(self):
        assert_that(ann).is_equal_to(ann)


    def test_class_is_equal_to_failure(self):
        try:
            assert_that(fred).is_equal_to(nick)
            fail('should have raised error')
        except AssertionError as ex:
            msg_pattern = re.compile('Expected <<.*>> to be equal to <<.*>>, but was not')
            assert msg_pattern.search(str(ex))


    def test_dataclass_is_equal_to_failure(self):
        try:
            assert_that(ann).is_equal_to(kate)
            fail('should have raised error')
        except AssertionError as ex:
            expected_msg = "Expected <PersonDataclass(first_name='Ann', last_name='Doe', age=24)> to be equal to <PersonDataclass(first_name='Kate', last_name='Doe', age=35)>, but was not."
            assert_that(str(ex)).contains(expected_msg)
