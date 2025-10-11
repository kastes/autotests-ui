import pytest


@pytest.fixture
def order():
    return []


@pytest.fixture
def append_first(order):
    order.append(1)


@pytest.fixture
def append_second(order, append_first):
    order.extend([2])


@pytest.fixture(autouse=True)
def append_third(order, append_second):
    order += [3]


def test_order(order, request):
    print(request)
    assert order == [1, 2, 3]


# content of test_finalizers.py
def test_bar(fix_w_yield1, fix_w_yield2):
    print("test_bar")


@pytest.fixture
def fix_w_yield1():
    print("before_yield_1")
    yield
    print("after_yield_1")


@pytest.fixture
def fix_w_yield2():
    print("before_yield_2")
    yield
    print("after_yield_2")
