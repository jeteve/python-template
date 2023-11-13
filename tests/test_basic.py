"""Basic tests"""

# from jeteve_template.sample import add_one

from jeteve_template.sample import add_one

def test_trivial():
    """Trivial test"""
    assert True

def test_add_one():
    """Just testing add_one"""
    assert add_one(2) == 3
