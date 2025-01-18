# Miniräknare
# 1 Gör ett program som frågar användaren efter 3 tal. 
# Sedan ska det räkna ut vad summan blir, och skriva ut på konsolen. (summa: tal1 + tal2 + tal3)

# 2 Programmet ska tala om vilket som är det största talet, utan att använda Python-funktionen max. Använd i stället if/elif/else. 
# Fundera på om man kan lösa uppgiften på olika sätt.

# 3 Programmet ska tala om ifall två av talen är lika, eller alla tre är lika.

# 4 Programmet ska tala om vilket som är det mellersta talet. 
# Observera att det bara finns ett mellersta tal om alla tre är olika, eller alla tre är lika. 
# (Om talen skulle vara till exempel 2, 2, 5 så räknas inget av dem som mellerst i den här uppgiften.)

# För att testa systematiskt kan du göra en tabell. 
# Kör sedan programmet. Kontrollera att programmet skriver ut samma saker som du har skrivit in i tabellen. 
# Vi kallar talen t1, t2 och t3.
# Förslag på värden att testa med:  1 2 3, 1 3 2, 3 2 1, -1 -3 -1, 9 9 9, 32 32 16

# t1 | t2  |  t3 | Störst  |  Två lika? |  Tre lika? | Mellerst?
# --------------------------------------------------------------
# 1  | 2   |  3  | 3       |  nej       |  nej       | 2



t1 = float(input("Ange tal1: "))
t2 = float(input("Ange tal2: "))
t3 = float(input("Ange tal3: "))

sum = t1 + t2 + t3
print("Summan av talen är: " + str(sum))

# Störst tal
# if t1 > t2 and t1 > t3:
#     print("tal1 är störst: " + str(t1))
# elif t2 > t1 and t2 > t3:
#     print("tal2 är störst: "+ str(t2))
# elif t3 > t1 and t3 > t2:
#     print("tal3 är störst: " + str(t3))

# Stört tal
t_biggest = None
if t1 >= t2 and t1 >= t3:
    t_biggest = t1
elif t2 >= t1 and t2 >= t3:
    t_biggest = t2
elif t3 >= t1 and t3 >= t2:
    t_biggest = t3

if t_biggest is not None:
    print("Störst tal: " + str(t_biggest))

if t1 == t2 and t2 == t3:
    print("Alla är lika")
elif t1 == t2 or t1 == t3 or t2 == t3:
    print("Två tal är lika")
else:
    if t2 < t1 < t3 or t3 < t1 < t2:
        print("tal1 är mellersta talet: " + str(t1))
    elif t1 < t2 < t3 or t3 < t2 < t1:
        print("tal2 är mellersta talet: " + str(t2))
    elif t1 < t3 < t2 or t2 < t3 < t1:
        print("tal3 är mellersta talet: " + str(t3))
