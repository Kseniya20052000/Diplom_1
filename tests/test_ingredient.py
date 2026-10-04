from praktikum.ingredient import Ingredient

def test_ingredient_initialization():
    ingredient = Ingredient("filling", "Cheese", 120.0)
    
    assert ingredient.get_type() == "filling"
    assert ingredient.get_name() == "Cheese"
    assert ingredient.get_price() == 120.0


def test_ingredient_different_type():
    sauce = Ingredient("sauce", "Garlic", 50.5)
    
    assert sauce.get_type() == "sauce"
    assert sauce.get_name() == "Garlic"
    assert sauce.get_price() == 50.5
