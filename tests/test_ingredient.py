import allure
from praktikum.ingredient import Ingredient


@allure.title("Тип ингредиента корректно сохраняется при инициализации (filling)")
def test_ingredient_type_filling():
    ingredient = Ingredient("filling", "Cheese", 120.0)
    with allure.step("Проверяем тип ингредиента"):
        assert ingredient.get_type() == "filling"


@allure.title("Имя ингредиента корректно сохраняется при инициализации (filling)")
def test_ingredient_name_filling():
    ingredient = Ingredient("filling", "Cheese", 120.0)
    with allure.step("Проверяем имя ингредиента"):
        assert ingredient.get_name() == "Cheese"


@allure.title("Цена ингредиента корректно сохраняется при инициализации (filling)")
def test_ingredient_price_filling():
    ingredient = Ingredient("filling", "Cheese", 120.0)
    with allure.step("Проверяем цену ингредиента"):
        assert ingredient.get_price() == 120.0


@allure.title("Тип соуса корректно сохраняется при инициализации (sauce)")
def test_ingredient_type_sauce():
    sauce = Ingredient("sauce", "Garlic", 50.5)
    with allure.step("Проверяем тип соуса"):
        assert sauce.get_type() == "sauce"


@allure.title("Имя соуса корректно сохраняется при инициализации (sauce)")
def test_ingredient_name_sauce():
    sauce = Ingredient("sauce", "Garlic", 50.5)
    with allure.step("Проверяем имя соуса"):
        assert sauce.get_name() == "Garlic"


@allure.title("Цена соуса корректно сохраняется при инициализации (sauce)")
def test_ingredient_price_sauce():
    sauce = Ingredient("sauce", "Garlic", 50.5)
    with allure.step("Проверяем цену соуса"):
        assert sauce.get_price() == 50.5
