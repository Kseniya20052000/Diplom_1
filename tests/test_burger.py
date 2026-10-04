# tests/test_burger.py
from praktikum.burger import Burger


def test_set_buns_assigns_bun(burger, black_bun):
    """Проверяем, что булочка корректно устанавливается в бургер."""
    burger.set_buns(black_bun)
    assert burger.bun == black_bun


def test_add_ingredient_appends_to_list(burger, hot_sauce):
    """Проверяем, что ингредиент добавляется в конец списка."""
    burger.add_ingredient(hot_sauce)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == hot_sauce


def test_remove_ingredient_by_index(burger, hot_sauce, cutlet):
    """Проверяем удаление ингредиента по индексу."""
    burger.add_ingredient(hot_sauce)
    burger.add_ingredient(cutlet)
    
    # Было 2 ингредиента
    assert len(burger.ingredients) == 2
    
    # Удаляем первый (индекс 0)
    burger.remove_ingredient(0)
    
    # Остался 1 ингредиент, и это cutlet
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == cutlet


def test_move_ingredient_changes_order(burger, hot_sauce, cutlet):
    """Проверяем перемещение ингредиента на новую позицию."""
    burger.add_ingredient(hot_sauce)      # индекс 0
    burger.add_ingredient(cutlet)         # индекс 1
    
    # Перемещаем hot_sauce (индекс 0) на позицию 1
    burger.move_ingredient(0, 1)
    
    assert burger.ingredients[0] == cutlet
    assert burger.ingredients[1] == hot_sauce


def test_get_price_calculates_correctly(burger, black_bun, hot_sauce, cutlet):
    """Проверяем расчёт цены: булочка * 2 + все ингредиенты."""
    burger.set_buns(black_bun)           # цена 100
    burger.add_ingredient(hot_sauce)    # цена 50
    burger.add_ingredient(cutlet)       # цена 80
    
    expected_price = (black_bun.get_price() * 2) + hot_sauce.get_price() + cutlet.get_price()
    # 100*2 + 50 + 80 = 330
    
    assert burger.get_price() == expected_price


def test_get_receipt_format_and_price(burger, black_bun, hot_sauce, cutlet):
    """Проверяем формат чека и что в нём указана правильная цена."""
    burger.set_buns(black_bun)
    burger.add_ingredient(hot_sauce)
    burger.add_ingredient(cutlet)
    
    receipt = burger.get_receipt()
    
    # Проверяем наличие ключевых строк
    assert "(==== black bun ====" in receipt
    assert "= sauce hot sauce =" in receipt.lower()
    assert "= filling cutlet =" in receipt.lower()
    assert f"Price: {burger.get_price()}" in receipt
