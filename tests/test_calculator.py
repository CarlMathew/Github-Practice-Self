from domain.calculator import add, multiplaction


def test_add():
    assert add(5, 2) == 7


def test_multiplaction():
    assert multiplaction(5 * 5) == 25