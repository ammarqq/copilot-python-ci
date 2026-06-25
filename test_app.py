# use pytest to test the functions in app.py file
from app import add_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(-5, -7) == -12
    assert add_numbers(2.5, 0.5) == 3.0


