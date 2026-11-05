import pytest
import allure

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


# Хелпер: создаёт бургер. Гибкий, но локальный (только для этого файла).

def make_burger(bun_name="black bun", bun_price=100, ingredients=()):
    burger = Burger()
    burger.set_buns(Bun(bun_name, bun_price))
    for ing_type, name, price in ingredients:
        burger.add_ingredient(Ingredient(ing_type, name, price))
    return burger


@allure.title("set_buns сохраняет переданную булочку")
def test_set_buns_stores_bun():
    burger = Burger()
    bun = Bun("white bun", 200)
    burger.set_buns(bun)
    assert burger.bun is bun


@allure.title("Новый бургер не содержит ингредиентов")
def test_new_burger_has_no_ingredients():
    assert Burger().ingredients == []


@allure.title("add_ingredient добавляет ингредиент в список")
def test_add_ingredient_appends():
    burger = Burger()
    ingredient = Ingredient("sauce", "hot sauce", 100)
    burger.add_ingredient(ingredient)
    assert burger.ingredients == [ingredient]


@allure.title("add_ingredient позволяет добавить несколько ингредиентов (порядок сохраняется)")
def test_add_ingredient_keeps_order():
    burger = Burger()
    sauce = Ingredient("sauce", "hot sauce", 100)
    filling = Ingredient("filling", "cutlet", 100)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)
    assert burger.ingredients == [sauce, filling]


@allure.title("remove_ingredient удаляет ингредиент по индексу")
@pytest.mark.parametrize(
    "recipe, index, expected",
    [
        ([("sauce", "hot sauce", 100)], 0, []),
        (
            [("sauce", "hot sauce", 100), ("filling", "cutlet", 100)],
            0,
            [("filling", "cutlet", 100)],
        ),
        (
            [("sauce", "hot sauce", 100), ("filling", "cutlet", 100)],
            1,
            [("sauce", "hot sauce", 100)],
        ),
    ],
)
def test_remove_ingredient_removes_by_index(recipe, index, expected):
    burger = make_burger(ingredients=recipe)
    burger.remove_ingredient(index)

    assert [
        (i.get_type(), i.get_name(), i.get_price()) for i in burger.ingredients
    ] == expected


@allure.title("move_ingredient перемещает ингредиент с одного индекса на другой")
@pytest.mark.parametrize(
    "recipe, old_index, new_index, expected",
    [
        (
            [("sauce", "hot sauce", 100), ("filling", "cutlet", 100)],
            1,
            0,
            [("filling", "cutlet", 100), ("sauce", "hot sauce", 100)],
        ),
        (
            [
                ("sauce", "hot sauce", 100),
                ("filling", "cutlet", 100),
                ("filling", "dinosaur", 200),
            ],
            0,
            2,
            [("filling", "cutlet", 100), ("filling", "dinosaur", 200), ("sauce", "hot sauce", 100)],
        ),
    ],
)
def test_move_ingredient_moves_to_new_index(recipe, old_index, new_index, expected):
    burger = make_burger(ingredients=recipe)
    burger.move_ingredient(old_index, new_index)

    assert [
        (i.get_type(), i.get_name(), i.get_price()) for i in burger.ingredients
    ] == expected


@allure.title("get_price считает цену как две булки плюс ингредиенты")
@pytest.mark.parametrize(
    "bun_price, recipe, expected",
    [
        (100, [], 200),                     
        (100.5, [("sauce", "hot sauce", 100)], 301),  
        (200, [("filling", "cutlet", 100), ("filling", "dinosaur", 200)], 700), 
    ],
)
def test_get_price_counts_buns_and_ingredients(bun_price, recipe, expected):
    burger = Burger()
    burger.set_buns(Bun("black bun", bun_price))
    for ing_type, name, price in recipe:
        burger.add_ingredient(Ingredient(ing_type, name, price))
    assert burger.get_price() == expected


@allure.title("get_receipt возвращает чек целиком, строка в строку (параметризованный тест)")
@pytest.mark.parametrize(
    "bun_name, bun_price, recipe, expected",
    [
        
        (
            "black bun", 100, [],
            "(==== black bun ====)\n(==== black bun ====)\n\nPrice: 200",
        ),
        
        (
            "black bun", 100, [("sauce", "hot sauce", 100)],
            "(==== black bun ====)\n= sauce hot sauce =\n(==== black bun ====)\n\nPrice: 300",
        ),
        
        (
            "white bun", 200, [("filling", "cutlet", 100), ("sauce", "chili sauce", 300)],
            "(==== white bun ====)\n= filling cutlet =\n= sauce chili sauce =\n(==== white bun ====)\n\nPrice: 800",
        ),
    ],
)
def test_get_receipt_returns_exact_receipt(bun_name, bun_price, recipe, expected):
    burger = Burger()
    burger.set_buns(Bun(bun_name, bun_price))
    for ing_type, name, price in recipe:
        burger.add_ingredient(Ingredient(ing_type, name, price))

   
    assert burger.get_receipt() == expected
