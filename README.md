# pytest-assert-that

It is a fork of the [assertpy](https://github.com/assertpy/assertpy) - assertions library for testing in Python with a nice fluent API. Main feature of pytest_assert_that is that pytest assertions rewritings (introspection) work!


## Usage

Just import the `assert_that` object, and away you go...

```py
from pytest_assert_that import assert_that

def test_something():
    assert_that(1 + 2).is_equal_to(3)
    assert_that('foobar').is_length(6).starts_with('foo').ends_with('bar')
    assert_that(['a', 'b', 'c']).contains('a').does_not_contain('x')
```

`pytest_assert_that` works best with a python test runner [pytest](http://pytest.org/).


## Installation

### Install via pip

Just install with:

```
pip install git+https://github.com/ExplorerOL/pytest-assert-that.git
```

## Docs

All assertions, with usage examples, are documented here:  
https://assertpy.github.io/docs.html

And there are hundreds of examples below.  Read on...

### Pytest assertions rewriting
In case of using pytest [pytest assertions rewriting](https://docs.pytest.org/en/9.0.x/how-to/assert.html#assertion-introspection-details) is used by default. It makes assertion error messages more verbose and detailed.
For example in case of dictionaries assertions and -vv pytest option
```py
ACTUAL_DICT = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
EXPECTED_DICT = {'key1': 'value1', 'key2': 'value2', 'key3': 'value33'}
assert_that(ACTUAL_DICT).is_equal_to(EXPECTED_DICT)
```
error message is
```py
AssertionError: Expected <{.., 'key3': 'value3'}> to be equal to <{.., 'key3': 'value33'}>, but was not.
assert {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} == {'key1': 'value1', 'key2': 'value2', 'key3': 'value33'}

  Common items:
  {'key1': 'value1', 'key2': 'value2'}
  Differing items:
  {'key3': 'value3'} != {'key3': 'value33'}

  Full diff:
    {
        'key1': 'value1',
        'key2': 'value2',
  -     'key3': 'value33',
  ?                    -
  +     'key3': 'value3',
    }
```
instead of 
```py
AssertionError: Expected <{.., 'key3': 'value3'}> to be equal to <{.., 'key3': 'value33'}>, but was not.
```
If that behaviour is undesired, configure assert_that not to use pytest assertions rewriting:
```py
assert_that.configure(is_native_assert=False)
```

All examples are same as for [assertpy](https://github.com/assertpy/assertpy)


## License

All files are licensed under the BSD 3-Clause License as follows:

> Copyright (c) 2015-2019, Activision Publishing, Inc.
> All rights reserved.
>
> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
>
> 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
>
> 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
>
> 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
>
> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
