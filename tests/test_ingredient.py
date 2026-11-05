import pytest
import allure
from praktikum.ingredient import Ingredient


@allure.title("get_type возвращает тип, переданный при инициализации")
@pytest.mark.parametrize(
    "ing_type, name, price",
    [
        ("filling", "Cheese", 120.0),
        ("sauce", "Garlic", 50.5),
        ("filling", "Cutlet", 150.0),
        ("sauce", "Chili", 60.0),
    ],
)
def test_ingredient_get_type_returns_passed_type(ing_type, name, price):
    ingredient = Ingredient(ing_type, name, price)
    assert ingredient.get_type() == ing_type


@allure.title("get_name возвращает имя, переданное при инициализации")
@pytest.mark.parametrize(
    "ing_type, name, price",
    [
        ("filling", "Cheese", 120.0),
        ("sauce", "Garlic", 50.5),
    ],
)
def test_ingredient_get_name_returns_passed_name(ing_type, name, price):
    ingredient = Ingredient(ing_type, name, price)
    assert ingredient.get_name() == name


@allure.title("get_price возвращает цену, переданную при инициализации")
@pytest.mark.parametrize(
    "ing_type, name, price",
    [
        ("filling", "Cheese", 120.0),
        ("sauce", "Garlic", 50.5),
    ],
)
def test_ingredient_get_price_returns_passed_price(ing_type, name, price):
    ingredient = Ingredient(ing_type, name, price)
    assert ingredient.get_price() == price


@allure.title("Тип ингредиента строго соответствует переданному значению без приведения типов")
@pytest.mark.parametrize("ing_type", ["filling", "sauce"])
def test_ingredient_type_strictness(ing_type):
    ingredient = Ingredient(ing_type, "Test Ingredient", 99.9)
    assert ingredient.get_type() == ing_type
