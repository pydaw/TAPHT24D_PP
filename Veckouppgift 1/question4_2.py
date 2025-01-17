import math
# 2 
# Skriv ett program som räknar ut längden på hypotenusan i en rätvinklig triangel. 
# Användaren behöver skriva in längden på de två kortare sidorna.
# Tips 1: fråga en AI om formeln Pythagoras sats. Men var noga med att inte fråga efter kod som löser uppgiften!
# Tips 2: räkna ut roten med math.sqrt().

# Som testdata kan du använda triangeln med sidorna 3, 4 och 5:

#Testdata
# a = 3
# b = 4
# c = 5
print("Beräkna länd på sida c i en rätvinklig triangel, då längderna sidorna a och b är kända")
a = float(input("Ange längd på sida a: "))
b = float(input("Ange längd på sida b: "))

# Pythagoras sats:
# c^2 = a^2 + b^2 => c = sqrt(a^2 + b^2)
c = math.sqrt(a**2+b**2)
print("Kalkylerad hypotenusa (c): " + str(c))

