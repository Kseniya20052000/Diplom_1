import pytest
import allure

from praktikum.database import Database


@allure.title("База данных содержит корректное количество элементов (параметризованный тест)")
@pytest.mark.parametrize(
    "method_name, expected_count",
    [
        ("available_buns", 3),
        ("available_ingredients", 6),
    ],
)
def test_database_has_correct_counts(method_name, expected_count):
    db = Database()
    method = getattr(db, method_name)
    result = method()  

    with allure.step(f"Проверяем, что {method_name}() возвращает ровно {expected_count} элементов"):
        assert len(result) == expected_count


@allure.title("В базе данных присутствуют ожидаемые названия булочек")
@pytest.mark.parametrize(
    "expected_name",
    ["black bun", "white bun", "red bun"],
)
def test_database_contains_bun_names(expected_name):
    db = Database()
    names = [b.get_name() for b in db.available_buns()]  

    with allure.step(f"Проверяем наличие булочки '{expected_name}' в базе"):
        assert expected_name in names


@allure.title("В базе данных присутствуют ожидаемые названия ингредиентов")
@pytest.mark.parametrize(
    "expected_name",
    ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"],
)
def test_database_contains_ingredient_names(expected_name):
    db = Database()
    names = [i.get_name() for i in db.available_ingredients()]  

    with allure.step(f"Проверяем наличие ингредиента '{expected_name}' в базе"):
        assert expected_name in names


@allure.title("Методы базы данных возвращают списки")
@pytest.mark.parametrize(
    "method_name",
    ["available_buns", "available_ingredients"],
)
def test_database_methods_return_list(method_name):
    db = Database()
    method = getattr(db, method_name)
    result = method()  

    with allure.step(f"Проверяем, что {method_name}() возвращает список"):
        assert isinstance(result, list)
