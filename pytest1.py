import pytest

def add(x, y):

    return x + y
def test_add():
    assert add(2, 3) == 50
    assert add(0, 0) == 0

def test_add_negative():
    assert add(-7, -1) == -8
    

