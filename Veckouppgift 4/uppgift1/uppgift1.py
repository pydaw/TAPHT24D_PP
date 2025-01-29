# 1.Läsa och förstå kod - diskutera i grupp
# Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?

print("=========")

print("- 1a -")
def foo(t):
    print("test")

foo("hej")
print("=========")

print("- 1b -")
def fun1(x, y):
    return x * y

print(3, 5)
print("=========")

print("- 1c -")
def fun1(x, y):
    return x * y

print(fun1(3, 5))
print("=========")

print("- 1d -")
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)
print("=========")

print("- 1e -")
a = 5
def fun3(a):
    a += 1

a += 2
print(a)
print("=========")


print("- 1f -")
def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a)
print("=========")


print("- 1g -") 
# Funktionen "isinstance" kan kontrollera en variabels datatyp. Vad gör funktionen is_number? Går det att förbättra koden?
def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))

print("# Alternativ lösning 1 #")
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print(is_number(5.5))
print(is_number(42))

print("# Alternativ lösning 2 #")
def is_number(s):
    return isinstance(s, int) or isinstance(s, float)

print(is_number(5.5))
print(is_number(42))

print("# Alternativ lösning 3 #")
def is_number(s):
    return isinstance(s,(int, float))
    
print(is_number(5.5))
print(is_number(42))

print("=========")


print("- 1h -")
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

aw = average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
print(aw)

print("=========")


print("- 1i -") 
# En uppgift i tre delar:
# Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
# Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
# Rätta felen, så funktionen gör det den ska.

def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])


print("# Alternativ lösning #")
def find_min(numbers):
    counter = None
    for item in numbers:
        if counter is None:
            counter = item
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])
print("=========")
