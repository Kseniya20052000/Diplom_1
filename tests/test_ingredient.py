# tests/test_ingredient.py
import allure
from praktikum.ingredient import Ingredient


@allure.title("Проверка инициализации ингредиента и корректности геттеров")
def test_ingredient_initialization():
    """Проверяем, что конструктор корректно сохраняет тип, имя и цену ингредиента."""
    with allure.step("Создаём ингредиент-начинку: тип 'filling', название 'Cheese', цена 120.0"):
        ingredient = Ingredient("filling", "Cheese", 120.0)

    with allure.step("Проверяем тип ингредиента"):
        assert ingredient.get_type() == "filling", "Тип ингредиента не совпадает с ожидаемым ('filling')"

    with allure.step("Проверяем название ингредиента"):
        assert ingredient.get_name() == "Cheese", "Название ингредиента не совпадает с ожидаемым ('Cheese')"

    with allure.step("Проверяем цену ингредиента"):
        assert ingredient.get_price() == 120.0, "Цена ингредиента не совпадает с ожидаемой (120.0)"


@allure.title("Проверка корректной работы с другим типом ингредиента (соус)")
def test_ingredient_different_type():
    """Проверяем инициализацию ингредиента другого типа — соуса."""
    with allure.step("Создаём ингредиент-соус: тип 'sauce', название 'Garlic', цена 50.5"):
        sauce = Ingredient("sauce", "Garlic", 50.5)

    with allure.step("Проверяем тип соуса"):
        assert sauce.get_type() == "sauce", "Тип соуса не совпадает с ожидаемым ('sauce')"

    with allure.step("Проверяем название соуса"):
        assert sauce.get_name() == "Garlic", "Название соуса не совпадает с ожидаемым ('Garlic')"

    with allure.step("Проверяем цену соуса"):
        assert sauce.get_price() == 50.5, "Цена соуса не совпадает с ожидаемой (50.5)"
