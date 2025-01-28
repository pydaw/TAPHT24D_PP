import my_module1
import my_module2
import my_module3
import my_module4
import my_module5
import my_module6
import my_module7
import my_module8


# 1 Skriv en funktion som tar en sträng som parameter. 
# När den anropas ska den skriva ut strängen och "är en fena på programmering". 
# Exempel:
# my_function("David") → "David är en riktig hacker"
my_module1.my_function("David")
my_module1.my_function("Daniel")


# 2a Skriv en funktion med namnet "eko". 
# När den anropas med en sträng ska den upprepa strängen, och skriva ut resultatet. 
# Exempel:
# eko("hej") → skriver ut "hejhej"
my_module2.eko("hej")


# 2b Lägg till en parameter "count", som avgör hur många ekon som ska skapas. 
# Exempel:
# eko("hej", 3) → skriver ut "hejhejhej"
my_module2.eko("hej", 3)


# 3 Följande kod ska sluta loopa efter 5 varv. 
# Flytta den in i en funktion och justera den enligt kommentaren.
# end = 5
# y = 1
# for x in range(1, 100):
#     y *= 2
#     # avsluta loopen med en if-sats här
# print(y)
my_module3.break_loop()


# 4 Skriv en funktion med namnet last. 
# Den ska ta en lista som parameter och returnera det sista elementet i listan.
# last([1, 2, 3]) → 3
print(my_module4.last([1, 2, 3]))
print(my_module4.last([1, 2]))
print(my_module4.last([1]))
# print(my_module4.last([]))


# 5 Skriv en funktion med namnet cut_edges. 
# Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista, 
# där den har tagit bort första och sista elementet.
# cut_edges([1, 2, 3, 4]) → [2, 3]
print(my_module5.cut_edges([1, 2, 3, 4]))
print(my_module5.cut_edges([1, 2, 3]))
print(my_module5.cut_edges([1, 2]))
# print(my_module5.cut_edges([1]))


# 6 Lös felen i koden.
# def increase(x):
#     return x
#     x += 1
# print(increase(1))
print(my_module6.increase(1))


# 7 Bygg en funktion med namnet average. 
# Den ska ta parametrar: x och y. Båda ska vara tal. 
# Funktionen ska returnera medelvärdet. 
# Till exempel så räknar man ut medelvärdet av 4 och 8 
# genom med formeln: (4 + 8) / 2, vilket blir 6.
# Tips: det kan vara enklare att använda fler variabler.
print(my_module7.average(4,8))
# print(my_module7.average("a","b"))
# print(my_module7.average("a",8))
# print(my_module7.average(4,"b"))


# 8 Gör en funktion som kan skriva ut innehållet i en lista lite snyggare. 
# Först ska funktionen tala om ifall listan är tom, eller hur många element den har. 
# Sedan ska funktionen skriva ut elementen i en punktlista. 
# Exempel:
# pretty_print(["a", "b", 3.14])
# Listan har 3 element:
# 1. a
# 2. b
# 3. 3.14
my_module8.pretty_print([])
my_module8.pretty_print(["a", "b", 3.14])