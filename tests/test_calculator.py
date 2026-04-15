

from domain.calculator import add, minus, multiplaction, average, division




def test_add():
    assert add(5, 2) == 7

def test_minus():
    assert minus(5, 2) == 3
def test_multiplaction():
    assert multiplaction(5, 5) == 25
def test_average():
    assert average([1,2,3]) == 2

def test_division():
    assert division(10, 2) == 5
