import allure
from praktikum.bun import Bun


@allure.title("Проверка имени булочки после инициализации")
def test_bun_name_after_init():
    bun = Bun("black bun", 100.5)
    with allure.step("Создаём булочку и проверяем имя"):
        assert bun.get_name() == "black bun"


@allure.title("Проверка цены булочки после инициализации")
def test_bun_price_after_init():
    bun = Bun("black bun", 100.5)
    with allure.step("Создаём булочку и проверяем цену"):
        assert bun.get_price() == 100.5


@allure.title("Разные экземпляры булочек хранят свои данные (проверка имени первой булочки)")
def test_bun_instances_keep_own_name_first():
    bun1 = Bun("white bun", 200)
    with allure.step("Проверяем имя первой булочки"):
        assert bun1.get_name() == "white bun"


@allure.title("Разные экземпляры булочек хранят свои данные (проверка цены первой булочки)")
def test_bun_instances_keep_own_price_first():
    bun1 = Bun("white bun", 200)
    with allure.step("Проверяем цену первой булочки"):
        assert bun1.get_price() == 200


@allure.title("Разные экземпляры булочек хранят свои данные (проверка имени второй булочки)")
def test_bun_instances_keep_own_name_second():
    bun2 = Bun("red bun", 300)
    with allure.step("Проверяем имя второй булочки"):
        assert bun2.get_name() == "red bun"


@allure.title("Разные экземпляры булочек хранят свои данные (проверка цены второй булочки)")
def test_bun_instances_keep_own_price_second():
    bun2 = Bun("red bun", 300)
    with allure.step("Проверяем цену второй булочки"):
        assert bun2.get_price() == 300


@allure.title("get_name возвращает строку")
def test_bun_get_name_returns_str():
    bun = Bun("test bun", 99.9)
    name = bun.get_name()
    with allure.step("Проверяем тип возвращаемого значения get_name"):
        assert isinstance(name, str)


@allure.title("get_price возвращает число (int или float)")
def test_bun_get_price_returns_number():
    bun = Bun("test bun", 99.9)
    price = bun.get_price()
    with allure.step("Проверяем тип возвращаемого значения get_price"):
        assert isinstance(price, (int, float))
