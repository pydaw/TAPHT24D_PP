from uppgift4 import Product, Order, ShoppingCart


# === Test Product ===
def test_Product_class():
    srewdriver = Product(1001,"Skruvmejselsats 6 delar", 199)
    assert  srewdriver.id == 1001
    assert  srewdriver.name == "Skruvmejselsats 6 delar"
    assert  srewdriver.price == 199


# === Test ShoppingCart ===
def test_ShoppingCart_class_init__property():
    shopping_cart = ShoppingCart(2000)
    
    assert shopping_cart.id == 2000
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

def test_ShoppingCart_class__cost():
    shopping_cart = ShoppingCart(2000)
    srewdriver = Product(1001,"Skruvmejselsats 6 delar", 199)
    hammer = Product(1002, "Hammare 500g", 149)

    shopping_cart.add_items_to_cart(srewdriver, 5) == True
    shopping_cart.add_items_to_cart(hammer, 6) == True
    assert shopping_cart.cost == 1889

def test_ShoppingCart_class__clear_cart():
    shopping_cart = ShoppingCart(2000)
    srewdriver = Product(1001,"Skruvmejselsats 6 delar", 199)
    hammer = Product(1002, "Hammare 500g", 149)
    shopping_cart.add_items_to_cart(srewdriver, 5)
    shopping_cart.add_items_to_cart(hammer, 6)

    # Check if cart have added items
    assert shopping_cart.cart == [[srewdriver, 5], [hammer, 6]]
    
    # Check if cart is empty
    assert shopping_cart.clear_cart() == True
    assert shopping_cart.cart == []

def test_ShoppingCart_class__order_items_in_cart():
    shopping_cart = ShoppingCart(2000)
    srewdriver = Product(1001,"Skruvmejselsats 6 delar", 199)
    hammer = Product(1002, "Hammare 500g", 149)
    shopping_cart.add_items_to_cart(srewdriver, 5)
    shopping_cart.add_items_to_cart(hammer, 6)

    # Check if cart have added items
    assert shopping_cart.cart == [[srewdriver, 5], [hammer, 6]]
    
    # Oder items in cart
    assert shopping_cart.order_items_in_cart() == True

    # Check that property "order have been placed" is set
    assert shopping_cart.order_has_been_placed == True

    # Oder items in cart again
    assert shopping_cart.order_items_in_cart() is None

    # Add item in chart after order
    assert shopping_cart.add_items_to_cart(srewdriver, 6) == False
    assert shopping_cart.cart == [[srewdriver, 5], [hammer, 6]]
    
    # Clear shopping cart after order
    assert shopping_cart.clear_cart() == False
    assert shopping_cart.cart == [[srewdriver, 5], [hammer, 6]]

    

# === Test Order ===
def test_Order_class__init_property():
    shopping_cart = ShoppingCart(2000)
    srewdriver = Product(1001,"Skruvmejselsats 6 delar", 199)
    hammer = Product(1002, "Hammare 500g", 149)
    shopping_cart.add_items_to_cart(srewdriver, 5)
    shopping_cart.add_items_to_cart(hammer, 6)
    shopping_cart.order_items_in_cart()

    order = Order(3000, shopping_cart.cart)

    assert order.id == 3000
    assert order.order == [[srewdriver, 5],[hammer, 6]]
    assert order.cost == 1889
    
