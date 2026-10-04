# tests/test_bun.py
from praktikum.bun import Bun


def test_bun_initialization():
    """Проверяем, что конструктор корректно сохраняет имя и цену."""
    bun = Bun("black bun", 100.5)
    
    assert bun.get_name() == "black bun"
    assert bun.get_price() == 100.5


def test_bun_different_values():
    """Проверяем, что разные экземпляры хранят свои собственные данные."""
    bun1 = Bun("white bun", 200)
    bun2 = Bun("red bun", 300)
    
    assert bun1.get_name() == "white bun"
    assert bun1.get_price() == 200
    
    assert bun2.get_name() == "red bun"
    assert bun2.get_price() == 300


def test_bun_getters_return_correct_types():
    """Проверяем типы возвращаемых значений (защита от будущих правок)."""
    bun = Bun("test bun", 99.9)
    
    name = bun.get_name()
    price = bun.get_price()
    
    assert isinstance(name, str)
    assert isinstance(price, (int, float))
