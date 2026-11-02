import pytest
import allure
from unittest.mock import MagicMock
from praktikum.burger import Burger


@allure.title("set_buns корректно устанавливает булочку (с моком)")
def test_set_buns_assigns_bun_with_mock():
    burger = Burger()
    
    mock_bun = MagicMock(spec=['get_name', 'get_price'])
    mock_bun.get_name.return_value = "mock bun"
    mock_bun.get_price.return_value = 999

    burger.set_buns(mock_bun)

    with allure.step("Проверяем, что атрибут bun содержит переданный мок-объект"):
        assert burger.bun is mock_bun


@pytest.mark.parametrize(
    "ingredient_type, ingredient_name, expected_count",
    [
        ("sauce", "hot sauce", 1),
        ("filling", "cutlet", 1),
        ("sauce", "sour cream", 2),  
    ],
)
@allure.title("add_ingredient добавляет ингредиент и увеличивает счетчик")
def test_add_ingredient_parametrized(ingredient_type, ingredient_name, expected_count):
    burger = Burger()
    
    
    mock_ing = MagicMock(spec=['get_type', 'get_name', 'get_price'])
    mock_ing.get_type.return_value = ingredient_type
    mock_ing.get_name.return_value = ingredient_name
    mock_ing.get_price.return_value = 100

    for _ in range(expected_count):
        burger.add_ingredient(mock_ing)

    with allure.step(f"Проверяем, что в списке ровно {expected_count} ингредиентов"):
        assert len(burger.ingredients) == expected_count
       
        assert burger.ingredients[-1] is mock_ing


@allure.title("remove_ingredient корректно удаляет по индексу (с моками)")
def test_remove_ingredient_by_index_with_mocks():
    burger = Burger()
    
    
    mock_sauce = MagicMock(spec=['get_type'])
    mock_cutlet = MagicMock(spec=['get_type'])

    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_cutlet)

    assert len(burger.ingredients) == 2
    
    burger.remove_ingredient(0)  

    with allure.step("Проверяем, что остался только cutlet и порядок сместился"):
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is mock_cutlet


@pytest.mark.parametrize(
    "start_idx, end_idx, expected_order",
    [
        (0, 1, [1, 0]),  
        (1, 0, [1, 0]),  
    ],
)
@allure.title("move_ingredient меняет порядок ингредиентов (параметризованный)")
def test_move_ingredient_parametrized(start_idx, end_idx, expected_order):
    burger = Burger()
    
    mock_a = MagicMock()
    mock_b = MagicMock()
    
    burger.add_ingredient(mock_a)
    burger.add_ingredient(mock_b)

    burger.move_ingredient(start_idx, end_idx)

    
    actual_objects = burger.ingredients
    
    with allure.step("Проверяем новый порядок объектов в списке"):
        if expected_order == [1, 0]:
            assert actual_objects[0] is mock_b
            assert actual_objects[1] is mock_a
        else:
            assert actual_objects[0] is mock_a
            assert actual_objects[1] is mock_b


@allure.title("get_price считает цену на основе моков (проверка логики сложения)")
def test_get_price_with_mocks():
    burger = Burger()
    
    mock_bun = MagicMock()
    mock_bun.get_price.return_value = 200
    
    mock_sauce = MagicMock()
    mock_sauce.get_price.return_value = 50
    
    mock_cutlet = MagicMock()
    mock_cutlet.get_price.return_value = 150

    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_cutlet)

    expected_total = (200 * 2) + 50 + 150  # 2 булочки + соус + котлета

    with allure.step("Сравниваем рассчитанную цену с ожидаемой суммой моков"):
        assert burger.get_price() == expected_total



@pytest.mark.usefixtures("black_bun", "hot_sauce", "cutlet")
@allure.title("Чек формируется полностью и точно соответствует ожидаемому формату")
def test_receipt_full_match(black_bun, hot_sauce, cutlet):
    burger = Burger()
    burger.set_buns(black_bun)
    burger.add_ingredient(hot_sauce)
    burger.add_ingredient(cutlet)

    expected_price = (black_bun.get_price() * 2) + hot_sauce.get_price() + cutlet.get_price()

    expected_receipt = (
        f"(==== {black_bun.get_name()} ====)\n"
        f"= {hot_sauce.get_type().lower()} {hot_sauce.get_name()} =\n"
        f"= {cutlet.get_type().lower()} {cutlet.get_name()} =\n"
        f"(==== {black_bun.get_name()} ====)\n\n" 
        f"Price: {expected_price}"
    )

    receipt = burger.get_receipt()

    with allure.step("Сравниваем чек целиком (строка в строку)"):
        assert receipt == expected_receipt, (
            f"Чек не совпадает с ожидаемым.\n"
            f"Ожидалось:\n{expected_receipt}\n"
            f"Получено:\n{receipt}"
        )


@pytest.mark.usefixtures("black_bun", "hot_sauce", "cutlet")
@allure.title("В чеке присутствуют все обязательные элементы (параметризованная проверка строк)")
@pytest.mark.parametrize(
    "expected_substring",
    [
        "(==== black bun ====",
        "= sauce hot sauce =",
        "= filling cutlet =",
        "Price:",
    ],
)
def test_receipt_contains_required_lines(black_bun, hot_sauce, cutlet, expected_substring):
    burger = Burger()
    burger.set_buns(black_bun)
    burger.add_ingredient(hot_sauce)
    burger.add_ingredient(cutlet)
    
    receipt = burger.get_receipt()

    with allure.step(f"Проверяем наличие подстроки: '{expected_substring}'"):
        assert expected_substring in receipt
