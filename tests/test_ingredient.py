import pytest
import allure
from unittest.mock import MagicMock
from praktikum.ingredient import Ingredient


@allure.title("Инициализация ингредиента: тип, имя и цена (параметризованный тест)")
@pytest.mark.parametrize(
    "ing_type, name, price",
    [
        ("filling", "Cheese", 120.0),
        ("sauce", "Garlic", 50.5),
        ("filling", "Cutlet", 150.0),
        ("sauce", "Chili", 60.0),
    ],
)
def test_ingredient_initialization(ing_type, name, price):
    ingredient = Ingredient(ing_type, name, price)

    with allure.step(f"Проверяем корректность данных для ингредиента '{name}'"):
        assert ingredient.get_type() == ing_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price


@allure.title("Тип ингредиента строго соответствует переданному значению (граничные проверки)")
@pytest.mark.parametrize(
    "ing_type",
    ["filling", "sauce"],
)
def test_ingredient_type_strictness(ing_type):
    ingredient = Ingredient(ing_type, "Test Ingredient", 99.9)

    with allure.step(f"Убеждаемся, что тип точно равен '{ing_type}' без приведения типов"):
        assert ingredient.get_type() == ing_type




@allure.title("Mock-объект корректно имитирует интерфейс Ingredient (проверка совместимости)")
def test_mock_ingredient_interface():
    
    mock_ingredient = MagicMock(spec=['get_type', 'get_name', 'get_price'])
    mock_ingredient.get_type.return_value = "filling"
    mock_ingredient.get_name.return_value = "Mock Cheese"
    mock_ingredient.get_price.return_value = 100.0

    
    result_type = mock_ingredient.get_type()
    result_name = mock_ingredient.get_name()
    result_price = mock_ingredient.get_price()

    with allure.step("Проверяем, что мок корректно возвращает заданные значения"):
        assert result_type == "filling"
        assert result_name == "Mock Cheese"
        assert result_price == 100.0


@allure.title("Система корректно обрабатывает мок-ингредиент вместо реального (проверка изоляции)")
def test_system_works_with_mock_ingredient():
    mock_ingredient = MagicMock(spec=['get_type', 'get_name', 'get_price'])
    mock_ingredient.get_type.return_value = "sauce"
    mock_ingredient.get_name.return_value = "Mock Garlic"
    mock_ingredient.get_price.return_value = 55.5

    
    assert mock_ingredient.get_type() == "sauce"
    assert mock_ingredient.get_name() == "Mock Garlic"
    assert mock_ingredient.get_price() == 55.5

    with allure.step("Убеждаемся, что мок можно использовать везде, где ожидается Ingredient"):
        
        assert callable(mock_ingredient.get_type)
        assert callable(mock_ingredient.get_name)
        assert callable(mock_ingredient.get_price)
