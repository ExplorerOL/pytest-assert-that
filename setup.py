from setuptools import setup
import pytest_assert_that

desc = """
pytest-assert-that
========

Simple assertions library for unit testing in Python with a nice fluent API. Supports both Python 2 and 3.

Usage
-----

Just import the ``assert_that`` function, and away you go...::

    from pytest_assert_that import assert_that

    def test_something():
        assert_that(1 + 2).is_equal_to(3)
        assert_that('foobar').is_length(6).starts_with('foo').ends_with('bar')
        assert_that(['a', 'b', 'c']).contains('a').does_not_contain('x')

Of course, pytest_assert_that works best with a python test runner like `pytest <http://pytest.org/>`_ (our favorite) or `Nose <http://nose.readthedocs.org/>`_.

Install
-------

The assertpy library is available via `PyPI <https://pypi.org/project/assertpy/>`_.
Just install with::

    pip install git+https://github.com/ExplorerOL/pytest-assert-that.git

"""

setup(
    name='pytest-assert-that',
    packages=['pytest_assert_that'],
    version=pytest_assert_that.__version__,
    description='Fork of the simple assertion library pytest-assert-that for testing in python with a fluent API',
    long_description=desc,
    author='Dmitry Vorobjev',
    author_email='explorerol.mailbox@gmail.com',
    url='https://github.com/ExplorerOL/pytest-assert-that',
    download_url='https://github.com/ExplorerOL/pytest-assert-that/pytest-assert-that/archive/%s.tar.gz' % pytest_assert_that.__version__,
    keywords=['pytest-assert-that', 'pytest_assert_that', 'test', 'testing', 'assert', 'assertion', 'assertthat', 'assert_that', 'pytest'],
    license='BSD',
    python_requires='>=3.8',
    extras_require={
        'pytest': ['pytest>=4.0'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing'])
