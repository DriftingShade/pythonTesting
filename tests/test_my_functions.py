import pytest
import my_functions as my_functions


def test_add():
    result = my_functions.add(2, 3)
    assert result == 5


def test_divide():
    result = my_functions.divide(6, 3)
    assert result == 2


def test_add_strings():
    result = my_functions.add("I like", " Python")
    assert result == "I like Python"


def test_divide_by_zero():
    my_functions.divide(10, 2)
