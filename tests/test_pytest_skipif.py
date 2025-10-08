import pytest
import sys

pytestmark = pytest.mark.skipif(condition=True, reason="Пропустить по условию.")


@pytest.mark.skipif(
    sys.version_info > (3, 7), reason="Требуется версия Python 3.6 или ниже."
)
def test_python_version_invalid():
    pass


@pytest.mark.skipif(
    sys.version_info < (3, 8), reason="Требуется версия Python 3.8 или выше."
)
def test_python_version_valid():
    pass
