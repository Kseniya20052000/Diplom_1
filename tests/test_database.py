# tests/test_database.py
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


def test_database_initializes_buns():
    """Проверяем, что при создании БД сразу добавляются 3 булочки."""
    db = Database()
    buns = db.available_buns()

    assert len(buns) == 3
    # Проверяем названия, чтобы убедиться, что это именно те булочки
    names = [b.get_name() for b in buns]
    assert "black bun" in names
    assert "white bun" in names
    assert "red bun" in names


def test_database_initializes_ingredients():
    """Проверяем, что при создании БД сразу добавляются ингредиенты (соусы и начинки)."""
    db = Database()
    ingredients = db.available_ingredients()

    assert len(ingredients) == 6
    names = [i.get_name() for i in ingredients]
    # Проверим хотя бы по одному представителю из каждой категории
    assert "hot sauce" in names  # соус
    assert "cutlet" in names      # начинка


def test_available_buns_returns_list():
    """Проверяем тип возвращаемого значения."""
    db = Database()
    result = db.available_buns()
    assert isinstance(result, list)


def test_available_ingredients_returns_list():
    """Проверяем тип возвращаемого значения."""
    db = Database()
    result = db.available_ingredients()
    assert isinstance(result, list)
