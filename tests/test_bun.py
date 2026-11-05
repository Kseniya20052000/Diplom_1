import pytest
import allure
from praktikum.bun import Bun


@allure.title("get_name возвращает имя, переданное при инициализации")
@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100.5),
        ("white bun", 200),
        ("red bun", 300),
    ],
)
def test_bun_get_name_returns_passed_name(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name


@allure.title("get_price возвращает цену, переданную при инициализации")
@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100.5),
        ("white bun", 200),
        ("red bun", 300),
    ],
)
def test_bun_get_price_returns_passed_price(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price


@allure.title("Новый экземпляр булочки хранит свои данные, когда создан другой экземпляр")
@pytest.mark.parametrize(
    "first, second",
    [
        (("white bun", 200), ("red bun", 300)),
        (("black bun", 100.5), ("white bun", 200)),
    ],
)
def test_bun_instances_keep_own_data(first, second):
    Bun(*first)
    bun = Bun(*second)
    assert (bun.get_name(), bun.get_price()) == second


@allure.title("get_name возвращает строку")
@pytest.mark.parametrize(
    "name, price",
    [("test bun", 99.9), ("", 0), ("very long bun name", 123.45)],
)
def test_bun_get_name_returns_str(name, price):
    bun = Bun(name, price)
    assert isinstance(bun.get_name(), str)


@allure.title("get_price возвращает число (int или float)")
@pytest.mark.parametrize(
    "name, price",
    [("int price bun", 100), ("float price bun", 99.9)],
)
def test_bun_get_price_returns_number(name, price):
    bun = Bun(name, price)
    assert isinstance(bun.get_price(), (int, float))
