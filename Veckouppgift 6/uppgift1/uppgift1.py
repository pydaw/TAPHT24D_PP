
print("=== 1 ===")
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


print("")
print("=== 2a ===")
# class Animal:
#     def make_noise(self):
#         print("Detta djur har vi inget ljud för.")

# class Dog(Animal):
#     def make_noise(self):
#     print("Voff!")

# class Cat(Animal):
#     def make_noise(shelf):
#         super().make_noise()
#         print("Mjau!")

# def sound_off(animal):
#     animal.make_noise()

# c = Cat()
# d = Dog()
# h = Rooster()
# sound_off([c, d, h])

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


print("")
print("=== 2b ===")
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
