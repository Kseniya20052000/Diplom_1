# tests/test_bun.py
import allure
from praktikum.bun import Bun


@allure.title("Проверка инициализации булочки и корректности геттеров")
def test_bun_initialization():
    """Проверяем, что конструктор корректно сохраняет имя и цену."""
    bun = Bun("black bun", 100.5)

    with allure.step("Создаём булочку с именем 'black bun' и ценой 100.5"):
        assert bun.get_name() == "black bun", "Имя булочки не совпадает с ожидаемым"
        assert bun.get_price() == 100.5, "Цена булочки не совпадает с ожидаемой"


@allure.title("Проверка независимости экземпляров булочек")
def test_bun_different_values():
    """Проверяем, что разные экземпляры хранят свои собственные данные."""
    bun1 = Bun("white bun", 200)
    bun2 = Bun("red bun", 300)

    with allure.step("Проверяем данные первой булочки (white bun)"):
        assert bun1.get_name() == "white bun", "Имя первой булочки не совпадает"
        assert bun1.get_price() == 200, "Цена первой булочки не совпадает"

    with allure.step("Проверяем данные второй булочки (red bun)"):
        assert bun2.get_name() == "red bun", "Имя второй булочки не совпадает"
        assert bun2.get_price() == 300, "Цена второй булочки не совпадает"


@allure.title("Проверка типов возвращаемых значений геттеров")
def test_bun_getters_return_correct_types():
    """Проверяем типы возвращаемых значений (защита от будущих правок)."""
    bun = Bun("test bun", 99.9)

    name = bun.get_name()
    price = bun.get_price()

    with allure.step("Убеждаемся, что get_name() возвращает строку"):
        assert isinstance(name, str), "get_name() должен возвращать строку"

    with allure.step("Убеждаемся, что get_price() возвращает число (int или float)"):
        assert isinstance(price, (int, float)), "get_price() должен возвращать число"
