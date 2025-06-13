"""Basic tests"""

# from jeteve_template.sample import add_one

from jeteve_template import hello
from jeteve_template.arithmetic import add_one
from jeteve_template.arithmetic.multiply import multiply_by_two
from jeteve_template.stringstuff import trim


def test_trivial():
    """Trivial test"""
    assert True


def test_multiply_by_two():
    """Just testing multiply_by_two"""
    assert multiply_by_two(2) == 4
    assert multiply_by_two(0) == 0
    assert multiply_by_two(-3) == -6
    assert multiply_by_two(1) == 2
    assert multiply_by_two(10) == 20


def test_hello():
    """Just testing hello"""
    assert hello("World") == "Hello, World!"
    assert hello("Alice") == "Hello, Alice!"
    assert hello("") == "Hello, !"
    assert hello(None) == "Hello, None!"
    assert hello("Bob") == "Hello, Bob!"


def test_add_one():
    """Just testing add_one"""
    assert add_one(2) == 3


def test_trim():
    """Just testing trim"""
    assert trim("  hello  ") == "hello"
    assert trim("") == ""
    assert trim(None) == ""
    assert trim("   ") == ""
    assert trim("test") == "test"
    assert trim("  test  ") == "test"
    assert trim("  test test  ") == "test test"
