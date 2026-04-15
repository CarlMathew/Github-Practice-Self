from domain.calculator import add, minus


def test_add():
    assert add(5, 2) == 7


def test_minus():
    assert minus(5, 2) == 3