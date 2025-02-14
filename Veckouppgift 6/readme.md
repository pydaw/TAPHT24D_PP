
# 1 Läsa och förstå kod - diskutera i grupp
Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?
  
  
1  
Vad gör följande kod?
```python
class SafeStorage:
    __data = None
    def get(self):
        return self.__data
    def put(self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)
```
  
Svar:  
- Programmet kommer att göra ett objekt som heter safe. Som anropar klassen SafeStorage.
- Man sparar strängen "Anakonda" i den privata egenskapen "__data"
- Man sparar egenskapen "__data" i variabeln "x"
- Man sparar sedan "Boaorm" till egenskapen "__data"
- Man sparar egenskapen "__data" i variabeln "y"
- Programmet kommer sedan skriva ut "Anakonda Boaorm"
  
  
2a  
Vad gör följande kod? Fixa eventuella fel.
```python
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
    print("Voff!")

class Cat(Animal):
    def make_noise(shelf):
        super().make_noise()
        print("Mjau!")

def sound_off(animal):
    animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()
sound_off([c, d, h])
```
  
Svar:  
- Koden kommer att göra tre objekt: c, d, h
- Koden anropar sedan funktionen "sound_off". Som är tänkt att anropar objektets metod "make_noise". Dock anropas funktionen med en lista, det känns som att det inte fungerar utan att någon form av loop. 
- Alla objekt ärver från klassen Animal.
- Hund klassen kommer inte att skriva ut "Voff" eftersom print funktionen inte är indenterad. samt är inte super anropad så metod i animals kommer att skrivas över.
- Katt klassen kommer att skriva ut: 
	"Detta djuret har vi inget ljud för"
	"Mjau!"
	Detta är för att metoden anropar super().make_moise(), dvs anropar Animals metod före sin egen metod.
- Klassen rooster finns inte så programmet kommer att göra en traceback.
  
Lösning:  
```python
# --- Justerad kod ---
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!")  # <--- Indenterad

class Cat(Animal):
    def make_noise(shelf):
        #super().make_noise()
        print("Mjau!")

class Rooster(Animal):
    def make_noise(shelf):
        print("kuckeliku!")

def sound_off(animal):
    animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()

# Bytt till att anropa funktionen flera ggr istället för att anropa med en lista
sound_off(c)
sound_off(d)
sound_off(h)
```
  
  
2b  
Lägg till en klass för ett annat djur, till exempel en guldfisk.
  
Lösning:  
```python
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!")  # <--- Indenterad

class Cat(Animal):
    def make_noise(shelf):
        #super().make_noise()
        print("Mjau!")

class Rooster(Animal):
    def make_noise(shelf):
        print("kuckeliku!")

class GoldFish(Animal):
    def make_noise(shelf):
        print("Blubb!")

def sound_off(animal):
    animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()
g = GoldFish()

# Bytt till att anropa funktionen flera ggr istället för att anropa med en lista
sound_off(c)
sound_off(d)
sound_off(h)
sound_off(g)

```
  
# 2 Länder
  
1a  
På Island bor det 383726 invånare och i Danmark 5961249. Skapa objekt för länderna. (Data från januari 2024. Avrunda befolkningen.)
```python
class Country:
    def __init__(self, name, pop):
        self.__name = name
        self.__population = pop

se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)
```
  
Lösning:  
Obs! Kan inte anväda "is" som variabel, eftersom det används av python. 
```python
class Country:
    def __init__(self, name, pop):
        self.__name = name
        self.__population = pop

se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)

# Skapar objekt för Island och Danmark
isl = Country("Island", 0.4)
dk = Country("Danmark", 6.0)
```
  
1b  
Lägg till en metod med namnet "print_info". 
Om man anropar den för Sverige-objektet ska den skriva ut: "I Sverige bor det 10.5 miljoner invånare". 
Funktionen ska använda sina egenskaper, så att den fungerar för de andra länderna också.
  
Lösning:  
```python
class Country:
 def __init__(self, name, pop):
     self.__name = name
     self.__population = pop
     
 def print_info(self):
     print(f"I {self.__name} bor det {self.__population} miljoner invånare")

se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)

# Skapar objekt för Island och Danmark
isl = Country("Island", 0.4)
dk = Country("Danmark", 6.0)

# Testar metoden
dk.print_info()
```

Testfall:
```log
I Danmark bor det 6.0 miljoner invånare
```
  
1c  
Lägg till landets area som en egenskap till klassen. 
Använd en parameter till konstruktorn, alltså `__init__` metoden. 
Ge arean ett default värde på None så att man inte måste ange arean när man skapar ett landsobjekt.
Exempel på default värde för en vanlig funktion:
```python
# y har default värde 10
def exempel(x, y=10):
    print(x + y)

exempel(2)  # skriver ut 12
```
  
Lösning:  
```python
class Country:
 def __init__(self, name, pop, area = None):
     self.__name = name
     self.__population = pop
     self.__area = area
     
 def print_info(self):
     print(f"I {self.__name} bor det {self.__population} miljoner invånare")

se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)

# Skapar objekt för Island och Danmark
isl = Country("Island", 0.4)
dk = Country("Danmark", 6.0)
```
  
1d  
Ändra i metoden "print_info" så att den skriver ut arean också, men bara om arean inte är None.
  
Lösning:  
```python
class Country:
 def __init__(self, name, pop, area = None):
     self.__name = name
     self.__population = pop
     self.__area = area
     
 def print_info(self):
     if self.__area is None:
	  print(f"I {self.__name} bor det {self.__population} miljoner invånare")
     else:
	  print(f"I {self.__name} bor det {self.__population} miljoner invånare, arean är {self.__area}km²")


se = Country("Sverige", 10.5, 447425)
no = Country("Norge", 5.5, 385207)
isl = Country("Island", 0.4, 103000)
dk = Country("Danmark", 6.0)

# Testar metoden
se.print_info()
dk.print_info()
```

Testfall:
```log
I Sverige bor det 10.5 miljoner invånare, arean är 447425km²
I Danmark bor det 6.0 miljoner invånare
```
  
1e  
Skapa en ny metod med namnet "add_language". Den ska lägga till ett av landets officiella språk. (Sverige har bara ett, men Finland har två språk (svenska och finska) och Schweiz har fyra.) För att kunna spara ett varierande antal behöver du använda en lista.
  
Lösning:  
```python
class Country:
 
 def __init__(self, name, pop, area = None):
     self.__name = name
     self.__population = pop
     self.__area = area
     self.__languages = list()
     
 def print_info(self):
     if self.__area is None:
	  print(f"I {self.__name} bor det {self.__population} miljoner invånare")
     else:
	  print(f"I {self.__name} bor det {self.__population} miljoner invånare, arean är {self.__area}km²")

 def add_language(self, language):
     self.__languages.append(language)


se = Country("Sverige", 10.5, 447425)
no = Country("Norge", 5.5, 385207)
isl = Country("Island", 0.4, 103000)
dk = Country("Danmark", 6.0)

```
  
1f  
Ändra i "print_info" så att den skriver ut alla officiella språk, på en ny rad.
  
Lösning:
```python
class Country:
 
 def __init__(self, name, pop, area = None):
     self.__name = name
     self.__population = pop
     self.__area = area
     self.__languages = list()
     
 def print_info(self):
     if self.__area is None:
	  print(f"I {self.__name} bor det {self.__population} miljoner invånare")
     else:
	  print(f"I {self.__name} bor det {self.__population} miljoner invånare, arean är {self.__area}km²")
     
     official_languages = str()
     for language in self.__languages: official_languages = official_languages + f"{language} "
     print(f"Officiella språk för landet är: {official_languages}")

 def add_language(self, language):
     self.__languages.append(language)


se = Country("Sverige", 10.5, 447425)
no = Country("Norge", 5.5, 385207)
isl = Country("Island", 0.4, 103000)
dk = Country("Danmark", 6.0)
fi = Country("Finland", 5.6, 338462)
ch = Country("Schweiz", 8.9, 41285)


# Testar metoden add_language
se.add_language("Svenska")

fi.add_language("Finska")
fi.add_language("Svenska")

ch.add_language("Tyska")
ch.add_language("Franska")
ch.add_language("Italienska")
ch.add_language("Rätoromanska")


# Testar metoden print_info
se.print_info()
dk.print_info()  # Kontrollerar tom lista
fi.print_info()
ch.print_info()
```
  
Testfall:
```log
I Sverige bor det 10.5 miljoner invånare, arean är 447425km²
Officiella språk för landet är: Svenska
I Danmark bor det 6.0 miljoner invånare
Officiella språk för landet är:
I Finland bor det 5.6 miljoner invånare, arean är 338462km²
Officiella språk för landet är: Finska Svenska
I Schweiz bor det 8.9 miljoner invånare, arean är 41285km²
Officiella språk för landet är: Tyska Franska Italienska Rätoromanska
```
  
# 3 Banken
Skapa en klass som representerar ett bankkonto. Banken ska kunna:
sätta in pengar (deposit)
ta up pengar (withdraw)
returnera nuvarande saldo (balance)
räkna ut ränta (apply_interest, lägger till räntan till kontot)
tala om ifall man har råd att betala en räkning (returnera True/False)

Gör en metod för varje funktion.

Skriv enhetstester för varje funktion. Använd gärna TDD-metoden, att börja med testfallen innan du skriver koden.
  
Lösning:
```python
class BankAccount():

    def __init__(self, savings = 0):
        self.__savings = savings

    def deposit(self, money):
        self.__savings += money

    def withdraw(self, money):
        self.__savings -= money

    def balance(self):
        return self.__savings

    def apply_interest(self, interest = 0.3):
        return self.__savings * (1 + interest)
    
    def afford(self, price):
        return price <= self.__savings
```
  
Testfall:
```python
from uppgift3 import BankAccount

def test_deposit():
    my_account = BankAccount()
    my_account.deposit(50)
    excepted = 50
    actual = my_account.balance()
    assert actual == excepted


def test_withdraw():
    my_account = BankAccount(50)
    my_account.withdraw(50)
    excepted = 0
    actual = my_account.balance()
    assert actual == excepted


def test_blance():
    my_account = BankAccount(50)
    excepted = 50
    actual = my_account.balance()
    assert actual == excepted


def test_apply_interest():
    my_account = BankAccount(50)
    excepted1 = 65
    actual1 = my_account.apply_interest()
    
    excepted2 = 100
    actual2 = my_account.apply_interest(1)
    
    assert actual1 == excepted1
    assert actual2 == excepted2


def test_afford():
    my_account = BankAccount(50)
    excepted1 = True
    actual1 = my_account.afford(50)
    
    excepted2 = False
    actual2 = my_account.afford(51)
    
    assert actual1 == excepted1
    assert actual2 == excepted2
```
  
```log
.....                                                                    [100%]
5 passed in 0.03s
Finished running tests!
```
  
# 4 Webbshop
Skapa klasser som representerar en webbshop:  
produkter (Product)  
beställningar (Order)  
kundvagn (ShoppingCart)  
  
Tips 1! Ge varje klass en egenskap "__id". Man kan använda den för att referera till ett annat objekt. Detta behövs eftersom både kundvagn och beställningar kommer att innehålla befintliga produkter.  
  
Tips 2! Du kan använda AI för att skapa realistisk testdata. Prova till att börja med:
"Skapa testdata för 10 produkter till en webbshop, som säljer verktyg. Visa datan i en tabell. Varje produkt ska ha namn, pris och ett unikt id."
  
  
Testdata från ChatGpt:  
  
| ID   | Produktnamn                 | Pris (SEK) |
| ---- | --------------------------- | ---------- |
| 1001 | Skruvmejselsats 6 delar     | 199        |
| 1002 | Hammare 500g                | 149        |
| 1004 | Cirkelsåg 1400W             | 1599       |
| 1005 | Hylsnyckelsats 94 delar     | 899        |
| 1006 | Tumstock 2m                 | 49         |
| 1008 | Polygrip tång 250mm         | 179        |
| 1009 | Spikpistol tryckluft        | 2199       |
| 1010 | Sågblad för sticksåg 5-pack | 129        |
| 1007 | Vattenpass 60cm             | 199        |
| 1003 | Borrmaskin 18V              | 1299       |
  
Köpprocess:  
1. Kundvagn
    - Innehåller produkter som kunden har valt men ännu inte köpt.
    - Kan uppdateras (lägga till/ta bort produkter).
    
2. Beställning
    - Skapas när kunden bekräftar köpet.
    - Är en permanent registrering av vad kunden har beställt.
    - Kan inte ändras hur som helst efter att den har skapats.
  
  
Lösning:
```python
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
        if not self.__order_has_been_placed:
            self.__cart.clear()
            return True
        else:
            return False
    
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
```
  
  
Testfall:
```python
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
    


```
  
```log
.......                                                                  [100%]
7 passed in 0.04s
Finished running tests!
```