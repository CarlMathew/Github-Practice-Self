
from domain.calculator import add, minus, multiplaction


def test_add():
    assert add(5, 2) == 7

def test_minus():
    assert minus(5, 2) == 3
def test_multiplaction():
    assert multiplaction(5 * 5) == 25
