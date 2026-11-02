import pytest
import allure
from unittest.mock import MagicMock
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


@allure.title("В базе данных присутствуют ожидаемые названия булочек (параметризованный тест)")
@pytest.mark.parametrize(
    "expected_name",
    ["black bun", "white bun", "red bun"],
)
def test_database_contains_bun_names(expected_name):
    db = Database()
    names = [b.get_name() for b in db.available_buns()]

    with allure.step(f"Проверяем наличие булочки '{expected_name}' в базе"):
        assert expected_name in names


@allure.title("В базе данных присутствуют ожидаемые названия ингредиентов (параметризованный тест)")
@pytest.mark.parametrize(
    "expected_name",
    ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"],
)
def test_database_contains_ingredient_names(expected_name):
    db = Database()
    names = [i.get_name() for i in db.available_ingredients()]

    with allure.step(f"Проверяем наличие ингредиента '{expected_name}' в базе"):
        assert expected_name in names


@allure.title("Методы базы данных возвращают списки (параметризованный тест типов)")
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




@allure.title("Database корректно обрабатывает моки булочек (проверка изоляции логики)")
def test_database_works_with_mock_buns():
    db = Database()

    
    mock_bun_1 = MagicMock(spec=['get_name', 'get_price'])
    mock_bun_1.get_name.return_value = "mock bun 1"
    mock_bun_1.get_price.return_value = 100

    mock_bun_2 = MagicMock(spec=['get_name', 'get_price'])
    mock_bun_2.get_name.return_value = "mock bun 2"
    mock_bun_2.get_price.return_value = 200

    db.buns = [mock_bun_1, mock_bun_2]

    result = db.available_buns()

    with allure.step("Проверяем, что метод возвращает подменённый список моков"):
        assert len(result) == 2
        assert result[0] is mock_bun_1
        assert result[1] is mock_bun_2


@allure.title("Database корректно обрабатывает моки ингредиентов (проверка изоляции логики)")
def test_database_works_with_mock_ingredients():
    db = Database()

    mock_ing_1 = MagicMock(spec=['get_type', 'get_name', 'get_price'])
    mock_ing_1.get_type.return_value = "sauce"
    mock_ing_1.get_name.return_value = "mock sauce"
    mock_ing_1.get_price.return_value = 50

    mock_ing_2 = MagicMock(spec=['get_type', 'get_name', 'get_price'])
    mock_ing_2.get_type.return_value = "filling"
    mock_ing_2.get_name.return_value = "mock filling"
    mock_ing_2.get_price.return_value = 70

    db.ingredients = [mock_ing_1, mock_ing_2]

    result = db.available_ingredients()

    with allure.step("Проверяем, что метод возвращает подменённый список моков"):
        assert len(result) == 2
        assert result[0] is mock_ing_1
        assert result[1] is mock_ing_2
