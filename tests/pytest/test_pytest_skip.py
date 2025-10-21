import pytest

pepxect = pytest.importorskip(
    modname="unknown", reason="Пропустить по условию: импорт модуля невозможен."
)


@pytest.mark.skip(reason="Функциональность в разработке")
def test_future_in_development():
    pass


@pytest.mark.skip(reason="Функциональность временно не работает")
class TestClass:
    def test_case1(self):
        pass

    def test_case2(self):
        pass
