import pytest
from configuration import *


def test_slogenie():
    assert 1 == 1, "Number is not"


def test_slogen():
    assert 1 + 3 == 4, "Правильно"


class Street():
    def test_solo():
        assert SON + NAME == 7, "Правильно"

def test_solo():
    assert Street == 7, "Правильно"


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

