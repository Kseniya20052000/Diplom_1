import pytest
import allure
from praktikum.bun import Bun


@allure.title("Проверка имени и цены булочек после инициализации (параметризованный тест)")
@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100.5),
        ("white bun", 200),
        ("red bun", 300),
    ],
)
def test_bun_name_and_price_after_init(name, price):
    bun = Bun(name, price)
    with allure.step(f"Создаём булочку '{name}' с ценой {price} и проверяем имя и цену"):
        assert bun.get_name() == name
        assert bun.get_price() == price


@allure.title("Разные экземпляры булочек хранят свои данные (проверка изоляции состояний)")
@pytest.mark.parametrize(
    "buns_data",
    [
        
        [("white bun", 200), ("red bun", 300)],
        [("black bun", 100.5), ("white bun", 200)],
    ],
)
def test_bun_instances_keep_own_data(buns_data):
    buns = [Bun(name, price) for name, price in buns_data]

    for i, (name, price) in enumerate(buns_data, start=1):
        with allure.step(f"Проверяем, что экземпляр {i} хранит свои данные"):
            assert buns[i - 1].get_name() == name
            assert buns[i - 1].get_price() == price


@allure.title("get_name возвращает строку (параметризованный тест с разными именами)")
@pytest.mark.parametrize(
    "name, price",
    [
        ("test bun", 99.9),
        ("", 0),
        ("very long bun name", 123.45),
    ],
)
def test_bun_get_name_returns_str(name, price):
    bun = Bun(name, price)
    result = bun.get_name()
    with allure.step("Проверяем, что get_name возвращает строку"):
        assert isinstance(result, str)


@allure.title("get_price возвращает число (int или float)")
@pytest.mark.parametrize(
    "name, price",
    [
        ("int price bun", 100),
        ("float price bun", 99.9),
    ],
)
def test_bun_get_price_returns_number(name, price):
    bun = Bun(name, price)
    result = bun.get_price()
    with allure.step("Проверяем, что get_price возвращает int или float"):
        assert isinstance(result, (int, float))
