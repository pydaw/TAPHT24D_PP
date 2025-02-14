
class Product():
    def __init__(self, id:int, name:str, price:float):
        self.__id = id
        self.__name = name
        self.__price = price
    
    def __str__(self):
        return f"Produkt: id-{self.__id} - {self.__name}"

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price    


class ShoppingCart():
    def __init__(self, id:int):
        self.__id = id
        self.__cart = list()
        self.__order_has_been_placed = False
        
    def __str__(self):
        return f"Kundvagn: id-{self.__id}"

    @property
    def id(self):
        return self.__id
    
    @property
    def cart(self):
        return self.__cart

    @property
    def cost(self):
        cost = 0
        for cart_pos in self.__cart:
            item = cart_pos[0]
            no_of_items = cart_pos[1]
            cost += item.price * no_of_items
        return cost
    
    @property
    def order_has_been_placed(self):
        return self.__order_has_been_placed 

    def add_items_to_cart(self, item:Product, no_of_items:int=1):
        # Check if same item already exist in cart    
        item_exists = False
        item_cart_index = None
        for cart_pos in self.__cart:
            if cart_pos[0] == item:
                item_exists = True
                item_cart_index = self.__cart.index(cart_pos)
                break
        
        if not self.__order_has_been_placed and not item_exists:
            self.__cart.append([item, no_of_items])
            return True
        elif not self.__order_has_been_placed and item_exists:
            self.__cart[item_cart_index][1] = no_of_items
            return True
        else:
            return False
        
    def clear_cart(self):
        self.__cart.clear()
    
    def order_items_in_cart(self):
        if not self.__order_has_been_placed:
            self.__order_has_been_placed = True
            return True
        else:
            return None


class Order():
    def __init__(self, id:int, order:list):
        self.__id = id

        # format of list: 
        # [[item (product), number_of_items],....]
        self.__order = order

        # Calculate cost of order
        cost = 0
        for order_pos in self.__order:
            item = order_pos[0]
            no_of_items = order_pos[1]
            cost += item.price * no_of_items
        self.__cost = cost

    def __str__(self):
        return f"Beställning: id-{self.__id}"

    @property
    def id(self):
        return self.__id
    
    @property
    def order(self):
        return self.__order
    
    @property
    def cost(self):
        return self.__cost

if __name__ == "__main__":
    shopping_cart = ShoppingCart(2000)
    srewdriver = Product(1001,"Skruvmejselsats 6 delar", 199)
    hammer = Product(1002, "Hammare 500g", 149)

    # Lägger till produkt1
    print(shopping_cart.add_items_to_cart(srewdriver)) # True
    print(shopping_cart.cart) # [[srewdriver, 1]]
    
    # Lägger till produkt2
    print(shopping_cart.add_items_to_cart(hammer, 6)) # True
    print(shopping_cart.cart) # [[srewdriver, 1], [hammer, 6]]
    
    # Ändring av antal produkt1
    print(shopping_cart.add_items_to_cart(srewdriver, 5)) # True
    print(shopping_cart.cart) # [[srewdriver, 5], [hammer, 6]]