from uppgift4 import *


# === Test Product ===
def test_Product_class():
    srewdriver = Product(1001,"Skruvmejselsats 6 delar", 199)
    assert  srewdriver.id == 1001
    assert  srewdriver.name == "Skruvmejselsats 6 delar"
    assert  srewdriver.price == 199


# === Test ShoppingCart ===
def test_ShoppingCart_class_init__property():
    shopping_cart = ShoppingCart(2000)
    assert shopping_cart.cart == []
    assert shopping_cart.cost == 0
    assert shopping_cart.order_has_been_placed == False

def test_ShoppingCart_class__add_items_to_cart():
    shopping_cart = ShoppingCart(2000)
    srewdriver = Product(1001,"Skruvmejselsats 6 delar", 199)
    hammer = Product(1002, "Hammare 500g", 149)

    # Lägger till produkt1
    assert shopping_cart.add_items_to_cart(srewdriver) == True
    assert shopping_cart.cart == [[srewdriver, 1]]
    
    # Lägger till produkt2
    assert shopping_cart.add_items_to_cart(hammer, 6) == True
    assert shopping_cart.cart == [[srewdriver, 1], [hammer, 6]]
    
    # Ändring av antal produkt1
    assert shopping_cart.add_items_to_cart(srewdriver, 5) == True
    assert shopping_cart.cart == [[srewdriver, 5], [hammer, 6]]