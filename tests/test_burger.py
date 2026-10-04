# tests/test_burger.py
import allure
from praktikum.burger import Burger


@allure.title("Установка булочки в бургер")
def test_set_buns_assigns_bun(burger, black_bun):
    """Проверяем, что булочка корректно устанавливается в бургер."""
    with allure.step("Устанавливаем булочку в бургер"):
        burger.set_buns(black_bun)

    with allure.step("Проверяем, что атрибут bun содержит переданную булочку"):
        assert burger.bun == black_bun, "Атрибут burger.bun не совпадает с переданной булочкой"


@allure.title("Добавление ингредиента в бургер")
def test_add_ingredient_appends_to_list(burger, hot_sauce):
    """Проверяем, что ингредиент добавляется в конец списка."""
    with allure.step("Добавляем ингредиент в бургер"):
        burger.add_ingredient(hot_sauce)

    with allure.step("Проверяем длину списка ингредиентов и его первый элемент"):
        assert len(burger.ingredients) == 1, "Количество ингредиентов не равно 1 после добавления"
        assert burger.ingredients[0] == hot_sauce, "Первый ингредиент не совпадает с добавленным"


@allure.title("Удаление ингредиента по индексу")
def test_remove_ingredient_by_index(burger, hot_sauce, cutlet):
    """Проверяем удаление ингредиента по индексу."""
    with allure.step("Добавляем два ингредиента: hot_sauce и cutlet"):
        burger.add_ingredient(hot_sauce)
        burger.add_ingredient(cutlet)
        assert len(burger.ingredients) == 2, "После добавления двух ингредиентов длина списка не равна 2"

    with allure.step("Удаляем ингредиент по индексу 0"):
        burger.remove_ingredient(0)

    with allure.step("Проверяем, что остался только cutlet"):
        assert len(burger.ingredients) == 1, "После удаления длина списка ингредиентов не равна 1"
        assert burger.ingredients[0] == cutlet, "Оставшийся ингредиент не совпадает с ожидаемым (cutlet)"


@allure.title("Перемещение ингредиента внутри бургера")
def test_move_ingredient_changes_order(burger, hot_sauce, cutlet):
    """Проверяем перемещение ингредиента на новую позицию."""
    with allure.step("Добавляем hot_sauce (индекс 0) и cutlet (индекс 1)"):
        burger.add_ingredient(hot_sauce)
        burger.add_ingredient(cutlet)

    with allure.step("Перемещаем hot_sauce с индекса 0 на индекс 1"):
        burger.move_ingredient(0, 1)

    with allure.step("Проверяем новый порядок ингредиентов"):
        assert burger.ingredients[0] == cutlet, "Первый элемент списка не совпадает с ожидаемым (cutlet)"
        assert burger.ingredients[1] == hot_sauce, "Второй элемент списка не совпадает с ожидаемым (hot_sauce)"


@allure.title("Расчёт итоговой цены бургера")
def test_get_price_calculates_correctly(burger, black_bun, hot_sauce, cutlet):
    """Проверяем расчёт цены: булочка * 2 + все ингредиенты."""
    with allure.step("Настраиваем бургер: устанавливаем булочку и добавляем ингредиенты"):
        burger.set_buns(black_bun)
        burger.add_ingredient(hot_sauce)
        burger.add_ingredient(cutlet)

    with allure.step("Вычисляем ожидаемую цену"):
        expected_price = (black_bun.get_price() * 2) + hot_sauce.get_price() + cutlet.get_price()

    with allure.step(f"Сравниваем рассчитанную цену ({burger.get_price()}) с ожидаемой ({expected_price})"):
        assert burger.get_price() == expected_price, f"Цена не совпадает: ожидалось {expected_price}, получено {burger.get_price()}"


@allure.title("Проверка формата чека и отображения цены")
def test_get_receipt_format_and_price(burger, black_bun, hot_sauce, cutlet):
    """Проверяем формат чека и что в нём указана правильная цена."""
    with allure.step("Собираем бургер: ставим булочку и добавляем ингредиенты"):
        burger.set_buns(black_bun)
        burger.add_ingredient(hot_sauce)
        burger.add_ingredient(cutlet)

    with allure.step("Получаем чек"):
        receipt = burger.get_receipt()

    with allure.step("Проверяем наличие ключевых строк в чеке"):
        assert "(==== black bun ====" in receipt, "В чеке отсутствует строка с названием булочки"
        assert "= sauce hot sauce =" in receipt.lower(), "В чеке не найден соус hot sauce"
        assert "= filling cutlet =" in receipt.lower(), "В чеке не найдена начинка cutlet"
        assert f"Price: {burger.get_price()}" in receipt, "В чеке не указана итоговая цена"
