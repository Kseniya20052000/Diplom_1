import allure
from praktikum.burger import Burger


@allure.title("set_buns корректно устанавливает булочку в бургер")
def test_set_buns_assigns_bun(burger, black_bun):
    burger.set_buns(black_bun)
    with allure.step("Проверяем, что атрибут bun содержит переданную булочку"):
        assert burger.bun == black_bun


@allure.title("add_ingredient добавляет ингредиент в конец списка")
def test_add_ingredient_appends_to_list(burger, hot_sauce):
    burger.add_ingredient(hot_sauce)
    with allure.step("Проверяем, что ингредиент добавлен в конец списка"):
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == hot_sauce


@allure.title("remove_ingredient корректно удаляет ингредиент по индексу")
def test_remove_ingredient_by_index(burger, hot_sauce, cutlet):
    burger.add_ingredient(hot_sauce)
    burger.add_ingredient(cutlet)
    assert len(burger.ingredients) == 2  # это подготовка
    burger.remove_ingredient(0)
    with allure.step("Проверяем, что после удаления остался только cutlet"):
        assert burger.ingredients[0] == cutlet


@allure.title("move_ingredient корректно меняет порядок ингредиентов")
def test_move_ingredient_changes_order(burger, hot_sauce, cutlet):
    burger.add_ingredient(hot_sauce)
    burger.add_ingredient(cutlet)
    burger.move_ingredient(0, 1)
    with allure.step("Проверяем новый порядок ингредиентов"):
        assert burger.ingredients[1] == hot_sauce


@allure.title("get_price корректно считает итоговую цену бургера")
def test_get_price_calculates_correctly(burger, black_bun, hot_sauce, cutlet):
    burger.set_buns(black_bun)
    burger.add_ingredient(hot_sauce)
    burger.add_ingredient(cutlet)
    expected_price = (black_bun.get_price() * 2) + hot_sauce.get_price() + cutlet.get_price()
    with allure.step("Сравниваем рассчитанную цену с ожидаемой"):
        assert burger.get_price() == expected_price


@allure.title("В чеке присутствует строка с названием булочки")
def test_receipt_contains_bun_line(burger, black_bun, hot_sauce, cutlet):
    burger.set_buns(black_bun)
    burger.add_ingredient(hot_sauce)
    burger.add_ingredient(cutlet)
    receipt = burger.get_receipt()
    with allure.step("Проверяем наличие строки с булочкой в чеке"):
        assert "(==== black bun ====" in receipt


@allure.title("В чеке присутствует упоминание соуса")
def test_receipt_contains_sauce_line(burger, black_bun, hot_sauce, cutlet):
    burger.set_buns(black_bun)
    burger.add_ingredient(hot_sauce)
    burger.add_ingredient(cutlet)
    receipt = burger.get_receipt()
    with allure.step("Проверяем наличие упоминания соуса в чеке"):
        assert "= sauce hot sauce =" in receipt.lower()


@allure.title("В чеке присутствует упоминание начинки")
def test_receipt_contains_filling_line(burger, black_bun, hot_sauce, cutlet):
    burger.set_buns(black_bun)
    burger.add_ingredient(hot_sauce)
    burger.add_ingredient(cutlet)
    receipt = burger.get_receipt()
    with allure.step("Проверяем наличие упоминания начинки в чеке"):
        assert "= filling cutlet =" in receipt.lower()


@allure.title("Чек формируется полностью и точно соответствует ожидаемому формату")
def test_receipt_full_match(burger, black_bun, hot_sauce, cutlet):
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