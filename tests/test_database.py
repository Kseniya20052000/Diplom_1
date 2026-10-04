# tests/test_database.py
import allure
from praktikum.database import Database


@allure.title("Проверка инициализации булочек в базе данных")
def test_database_initializes_buns():
    """Проверяем, что при создании БД сразу добавляются 3 булочки."""
    with allure.step("Создаём экземпляр базы данных и получаем список булочек"):
        db = Database()
        buns = db.available_buns()

    with allure.step("Проверяем, что в базе ровно 3 булочки"):
        assert len(buns) == 3, "В базе данных неверное количество булочек: ожидалось 3"

    with allure.step("Собираем названия булочек и проверяем наличие ожидаемых значений"):
        names = [b.get_name() for b in buns]
        assert "black bun" in names, "В списке булочек отсутствует 'black bun'"
        assert "white bun" in names, "В списке булочек отсутствует 'white bun'"
        assert "red bun" in names, "В списке булочек отсутствует 'red bun'"


@allure.title("Проверка инициализации ингредиентов в базе данных")
def test_database_initializes_ingredients():
    """Проверяем, что при создании БД сразу добавляются ингредиенты (соусы и начинки)."""
    with allure.step("Создаём экземпляр базы данных и получаем список ингредиентов"):
        db = Database()
        ingredients = db.available_ingredients()

    with allure.step("Проверяем, что в базе ровно 6 ингредиентов"):
        assert len(ingredients) == 6, "В базе данных неверное количество ингредиентов: ожидалось 6"

    with allure.step("Собираем названия ингредиентов и проверяем наличие представителей категорий"):
        names = [i.get_name() for i in ingredients]
        assert "hot sauce" in names, "В списке ингредиентов отсутствует 'hot sauce' (соус)"
        assert "cutlet" in names, "В списке ингредиентов отсутствует 'cutlet' (начинка)"


@allure.title("Проверка типа возвращаемого значения available_buns")
def test_available_buns_returns_list():
    """Проверяем тип возвращаемого значения."""
    with allure.step("Создаём базу данных и запрашиваем список булочек"):
        db = Database()
        result = db.available_buns()

    with allure.step("Убеждаемся, что метод возвращает список"):
        assert isinstance(result, list), "Метод available_buns должен возвращать список"


@allure.title("Проверка типа возвращаемого значения available_ingredients")
def test_available_ingredients_returns_list():
    """Проверяем тип возвращаемого значения."""
    with allure.step("Создаём базу данных и запрашиваем список ингредиентов"):
        db = Database()
        result = db.available_ingredients()

    with allure.step("Убеждаемся, что метод возвращает список"):
        assert isinstance(result, list), "Метод available_ingredients должен возвращать список"
