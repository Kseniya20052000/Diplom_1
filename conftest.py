# conftest.py
import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def black_bun():
    return Bun("black bun", 100)

@pytest.fixture
def hot_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)

@pytest.fixture
def cutlet():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 80)
