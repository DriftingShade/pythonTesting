import pytest
import my_functions as my_functions


def test_add():
    result = my_functions.add(2, 3)
    assert result == 5


def test_divide():
    result = my_functions.divide(6, 3)
    assert result == 2
