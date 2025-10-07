import pytest


def test_first():
    assert 1 == 1
    print("Привет")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_assert_positive_case():
    assert (2 + 2) == 4


def test_assert_negative_case():
    assert (2 + 2) == 5


class TestUserLogin:
    def test_1(self):
        assert False, "Это ошибка!"

    def test_2(self):
        assert True
