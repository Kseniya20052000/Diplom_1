import allure
from praktikum.database import Database


@allure.title("База данных содержит ровно 3 булочки")
def test_database_has_three_buns():
    db = Database()
    buns = db.available_buns()
    with allure.step("Проверяем количество булочек в базе"):
        assert len(buns) == 3


@allure.title("В базе данных присутствует булочка black bun")
def test_database_contains_black_bun():
    db = Database()
    names = [b.get_name() for b in db.available_buns()]
    with allure.step("Проверяем наличие black bun в списке булочек"):
        assert "black bun" in names


@allure.title("В базе данных присутствует булочка white bun")
def test_database_contains_white_bun():
    db = Database()
    names = [b.get_name() for b in db.available_buns()]
    with allure.step("Проверяем наличие white bun в списке булочек"):
        assert "white bun" in names


@allure.title("В базе данных присутствует булочка red bun")
def test_database_contains_red_bun():
    db = Database()
    names = [b.get_name() for b in db.available_buns()]
    with allure.step("Проверяем наличие red bun в списке булочек"):
        assert "red bun" in names


@allure.title("База данных содержит ровно 6 ингредиентов")
def test_database_has_six_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    with allure.step("Проверяем количество ингредиентов в базе"):
        assert len(ingredients) == 6


@allure.title("В базе данных присутствует ингредиент hot sauce")
def test_database_contains_hot_sauce():
    db = Database()
    names = [i.get_name() for i in db.available_ingredients()]
    with allure.step("Проверяем наличие hot sauce в списке ингредиентов"):
        assert "hot sauce" in names


@allure.title("В базе данных присутствует ингредиент cutlet")
def test_database_contains_cutlet():
    db = Database()
    names = [i.get_name() for i in db.available_ingredients()]
    with allure.step("Проверяем наличие cutlet в списке ингредиентов"):
        assert "cutlet" in names


@allure.title("available_buns возвращает список")
def test_available_buns_returns_list():
    db = Database()
    result = db.available_buns()
    with allure.step("Проверяем тип возвращаемого значения available_buns"):
        assert isinstance(result, list)


@allure.title("available_ingredients возвращает список")
def test_available_ingredients_returns_list():
    db = Database()
    result = db.available_ingredients()
    with allure.step("Проверяем тип возвращаемого значения available_ingredients"):
        assert isinstance(result, list)
