
# Uppgift1

1. Index variabeln börjar med värdet 5 ökas med 2 vid varje loop. Tills index kommer upp till limit då kommer programmet att avsluta while loopen. Dvs det kommer att printas: 5 7 9 11 13 15
2. for loopen kommer att skriva ut en tom rad när i = 5 annars kommer den att skriva ut i 0-9, vilket anges i range.
3. range6 ger att i kommer att ha värdet 0-5... sedan kommer den att köra count = 0+1+2+3+4+5 = 15
4. while loopen kommer att öka variabeln y med 1 varje loop. i while loopen kommer x att subtraheras med y värdet när y är udda. när y är jämt så kommer x adderas med yxy. while loopen avslutas när y kommer upp till 10
5. Fungerar bättre med: 
   print(f"detta funkar bättre: {message[4:8]}")
6. adderar 1 till y variabeln i if-satsen
```python
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y + 1: #<--ändrat detta så kommer den att rita ut strecket ett steg åt höger
            s += "#"
        else:
            s += "."
    print(s)
```


```log
----- 1 -----
5
7
9
11
13
15
----- 2 -----
0
1
2
3
4

6
7
8
9
----- 3 -----
15
----- 4 -----
x: 1, y: 2
x: -1, y: 3
x: 8, y: 4
x: 4, y: 5
x: 29, y: 6
x: 23, y: 7
x: 72, y: 8
x: 64, y: 9
x: 145, y: 10
----- 5 -----
_tim
detta funkar bättre: time
----- 6 -----
.#......
..#.....
...#....
....#...
.....#..
......#.
```


# Uppgift 2
Se kod

# Uppgift 3
Koden är indelad i 4 versioner (Nice to have anses som en egen vesision.)

Att testa de olika versionerna görs genom att ändra ´__vesion__´ variabeln till ett värde mellan 1-4.

Tesfall:
Version 1:
100
10, 20, 15

```log
Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 100
Skriv in ett belopp: quit
Det blir 100.0 kr totalt. Välkommen åter!


Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 10
Skriv in ett belopp: 20
Skriv in ett belopp: 15
Skriv in ett belopp: quit
Det blir 45.0 kr totalt. Välkommen åter!
```

Version 2:
100, 1 person
100, 2 personer
10, 10, 40 personer
30, 20, 30, 1 person

```log
Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 100
Skriv in ett belopp: quit
Hur många är ni? 1
Det blir 100.0 kr totalt, alltså 100.0 kr per person. Välkommen åter!

Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 100
Skriv in ett belopp: quit
Hur många är ni? 2
Det blir 100.0 kr totalt, alltså 50.0 kr per person. Välkommen åter!

Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 10
Skriv in ett belopp: 10
Skriv in ett belopp: quit
Hur många är ni? 40
Det blir 20.0 kr totalt, alltså 0.5 kr per person. Välkommen åter!

Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 30
Skriv in ett belopp: 20
Skriv in ett belopp: 30
Skriv in ett belopp: quit
Hur många är ni? 1
Det blir 80.0 kr totalt, alltså 80.0 kr per person. Välkommen åter!
```

Version 3:
50, 50 , 50, 3 personer, dricks = tom sträng
10, 20 , 70, 2 personer, dricks = 0%
10, 20 , 70, 2 personer, dricks = 20%
10, 20 , 70, 2 personer, dricks = -10% <--- inte bra att man kan ge minus dricks ändras till version 4


```log
Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 50
Skriv in ett belopp: 50
Skriv in ett belopp: 50
Skriv in ett belopp: quit
Hur många är ni? 3
Hur många procent i dricks? (tomt = 10%)
Det blir 165.0 kr totalt (varav 15.0 kr är dicks), alltså 55.0 kr per person (varav 5.0 kr är dricks). Välkommen åter! 

Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 10
Skriv in ett belopp: 20
Skriv in ett belopp: 70
Skriv in ett belopp: quit
Hur många är ni? 2
Hur många procent i dricks? (tomt = 10%) 0
Det blir 100.0 kr totalt (varav 0.0 kr är dicks), alltså 50.0 kr per person (varav 0.0 kr är dricks). Välkommen åter!  

Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 10
Skriv in ett belopp: 20
Skriv in ett belopp: 70
Skriv in ett belopp: quit
Hur många är ni? 2
Hur många procent i dricks? (tomt = 10%) 20
Det blir 120.0 kr totalt (varav 20.0 kr är dicks), alltså 60.0 kr per person (varav 10.0 kr är dricks). Välkommen åter!

Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 10
Skriv in ett belopp: 20
Skriv in ett belopp: 70
Skriv in ett belopp: quit
Hur många är ni? 2
Hur många procent i dricks? (tomt = 10%) -10
Det blir 90.0 kr totalt (varav -10.0 kr är dicks), alltså 45.0 kr per person (varav -5.0 kr är dricks). Välkommen åter! 
```

Version 4:
50, 50 , 50, 3 personer, dricks = tom sträng
10, 20 , 70, 2 personer, dricks = 0%
10, 20 , 70, 2 personer, dricks = 20%
10, 20 , 70, 2 personer, dricks = -10%, 10%

50, 50 , 50, 3 personer, dricks = fff
10, 10+, 20 , 70, 2 personer, dricks = 0%
10, 20 , 70, 1+ personer, -1 personer, dricks = 20%

```log
Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 50
Skriv in ett belopp: 50
Skriv in ett belopp: 50
Skriv in ett belopp: quit
Hur många är ni? 3
Hur många procent i dricks? (tomt = 10%)
Det blir 165.0 kr totalt (varav 15.0 kr är dicks), alltså 55.0 kr per person (varav 5.0 kr är dricks). Välkommen åter! 

Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 10
Skriv in ett belopp: 20
Skriv in ett belopp: 70
Skriv in ett belopp: quit
Hur många är ni? 2
Hur många procent i dricks? (tomt = 10%) 0
Det blir 100.0 kr totalt (varav 0.0 kr är dicks), alltså 50.0 kr per person (varav 0.0 kr är dricks). Välkommen åter!

Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 10
Skriv in ett belopp: 20
Skriv in ett belopp: 70
Skriv in ett belopp: quit
Hur många är ni? 2
Hur många procent i dricks? (tomt = 10%) 20
Det blir 120.0 kr totalt (varav 20.0 kr är dicks), alltså 60.0 kr per person (varav 10.0 kr är dricks). Välkommen åter!

Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 10
Skriv in ett belopp: 20
Skriv in ett belopp: 70
Skriv in ett belopp: quit
Hur många är ni? 2
Hur många procent i dricks? (tomt = 10%) -10
Hur många procent i dricks? (tomt = 10%) 10
Det blir 110.0 kr totalt (varav 10.0 kr är dicks), alltså 55.0 kr per person (varav 5.0 kr är dricks). Välkommen åter!

Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 50
Skriv in ett belopp: 50
Skriv in ett belopp: 50
Skriv in ett belopp: quit
Hur många är ni? 3
Hur många procent i dricks? (tomt = 10%) fff
Dicks skall skrivas in som ett decimal tal (>=0%)
Hur många procent i dricks? (tomt = 10%)
Det blir 165.0 kr totalt (varav 15.0 kr är dicks), alltså 55.0 kr per person (varav 5.0 kr är dricks). Välkommen åter!

Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 10
Skriv in ett belopp: 10+
Felaktig värde! Ange ett tal eller avsluta med 'quit'
Skriv in ett belopp: 20
Skriv in ett belopp: 70
Skriv in ett belopp: quit
Hur många är ni? 2
Hur många procent i dricks? (tomt = 10%) 0
Det blir 100.0 kr totalt (varav 0.0 kr är dicks), alltså 50.0 kr per person (varav 0.0 kr är dricks). Välkommen åter!

Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 10
Skriv in ett belopp: 20
Skriv in ett belopp: 70
Skriv in ett belopp: quit
Hur många är ni? 1+
Antal personer skall skrivas in som ett heltal
Hur många är ni? -1
Måste ange ett positivt heltal
Hur många är ni? 2
Hur många procent i dricks? (tomt = 10%) 20
Det blir 120.0 kr totalt (varav 20.0 kr är dicks), alltså 60.0 kr per person (varav 10.0 kr är dricks). Välkommen åter!
```


# Uppgift 4

Terminal fönstret kommer att rensas på text sedan kommer de olika figurerna att loopas igenom och visas i 3 sekunder.

Det är en while loop som aldrig kommer att avlutas.
Man avslutar programmet genom "ctrl+c"

# Uppgift 5
Koden är indelad i 2 versioner

Att testa de olika versionerna görs genom att ändra ´__vesion__´ variabeln till ett värde mellan 1-2.

Version1:

```log
Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?
Gissa: 50
Nej, det är för högt!
Gissa: 20
Nej, det är för lågt!
Gissa: 40
Nej, det är för lågt!
Gissa: 45
Nej, det är för högt!
Gissa: 44
Nej, det är för högt!
Gissa: 43
Det är rätt!! Du gjorde det på 6 gissningar.
```

Version2:
Har lagt till att man kollar att gissningen ligger 5 ifrån.
då läggs texten `"Nu börjar det brännas!\n"` ut innan texten som säger om man är för högt eller lågt. Har även justerat radbrytningar så utskriften ser lite bättre ut.


```log
Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?
Gissa: 50
Nej, det är för lågt!

Gissa: 70
Nej, det är för lågt!

Gissa: 80
Nej, det är för lågt!

Gissa: 90
Nej, det är för lågt!

Gissa: 100
Nu börjar det brännas!
Nej, det är för högt!

Gissa: 98
Nu börjar det brännas!
Nej, det är för högt!

Gissa: 97
Nu börjar det brännas!
Nej, det är för högt!

Gissa: 96
Det är rätt!! Du gjorde det på 8 gissningar.
```


# Uppgift 6

Koden är indelad i 3 versioner

Att testa de olika versionerna görs genom att ändra ´__vesion__´ variabeln till ett värde mellan 1-3.


Version1:

Kan göra lägga till i listan samt titta på den.
Kan bara titta på listan om den finns.

```log
** Todo list extravaganza **
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
quit. Avsluta
Välj ett alternativ: 1
Din lista är tom
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
quit. Avsluta
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra: måla huset
Ok, lade till "måla huset" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
quit. Avsluta
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra: klippa gräset
Ok, lade till "klippa gräset" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
quit. Avsluta
Välj ett alternativ: 1
+ måla huset
+ klippa gräset
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
quit. Avsluta
Välj ett alternativ: quit
Avslutar programmet
```

Version 2:

Fungerar som version1 fast man kan nu klarmarkera uppgifter.
Den klarmarkerade uppgiften raderas ut listan.
Man kan inte radera upgifter som inte finns med i listan.


```log
** Todo list extravaganza **
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 1
Din lista är tom
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 3
Ange vilken uppgift som skall klarmarkeras?: ddd
Kan inte hitta "ddd" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra: måla huset
Ok, lade till "måla huset" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra: klippa gräset
Ok, lade till "klippa gräset" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 1
+ måla huset
+ klippa gräset
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 3
Ange vilken uppgift som skall klarmarkeras?: klippa gräset
Ok, tagit bort "klippa gräset" från listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 1
+ måla huset
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: quit
Avslutar programmet
```


Version 3.

Fungerar som version1 o 2 men klarmarkerade uppgifter sparas i en separat lista.
Denna listan kan användas för att snabbare lägga till uppgiften igen, genom att välja index numret eller att välja att skriva in samma uppgiften igen. Uppgiften kommer då att raderas i klarmarkeringslistan och adderas i att göra listan.

```log
** Todo list extravaganza **
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 1
Din lista är tom
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 3
Ange vilken uppgift som skall klarmarkeras?: ddd
Kan inte hitta "ddd" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra (använd nummer för att välja gammal uppgift): måla huset
Ok, lade till "måla huset" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra (använd nummer för att välja gammal uppgift): klippa gräset
Ok, lade till "klippa gräset" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra (använd nummer för att välja gammal uppgift): måla staket
Ok, lade till "måla staket" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 1
+ måla huset
+ klippa gräset
+ måla staket
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 3
Ange vilken uppgift som skall klarmarkeras?: klippa gräset
Ok, tagit bort "klippa gräset" från listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 3
Klarmarkerade uppgifter:
0: klippa gräset

Ange vilken uppgift som skall klarmarkeras?: fff
Kan inte hitta "fff" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Klarmarkerade uppgifter:
0: klippa gräset

Skriv in en ny sak du måste komma ihåg att göra (använd nummer för att välja gammal uppgift): 0
Ok, lade till "klippa gräset" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 1
+ måla huset
+ måla staket
+ klippa gräset
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: quit
Avslutar programmet




** Todo list extravaganza **
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra (använd nummer för att välja gammal uppgift): test 1
Ok, lade till "test 1" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra (använd nummer för att välja gammal uppgift): test 2
Ok, lade till "test 2" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra (använd nummer för att välja gammal uppgift): test 4
Ok, lade till "test 4" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra (använd nummer för att välja gammal uppgift): test 3
Ok, lade till "test 3" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 1
+ test 1
+ test 2
+ test 4
+ test 3
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 3
Ange vilken uppgift som skall klarmarkeras?: test 3
Ok, tagit bort "test 3" från listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 3
Klarmarkerade uppgifter:
0: test 3

Ange vilken uppgift som skall klarmarkeras?: test 4
Ok, tagit bort "test 4" från listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 1
+ test 1
+ test 2
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Klarmarkerade uppgifter:
0: test 3
1: test 4

Skriv in en ny sak du måste komma ihåg att göra (använd nummer för att välja gammal uppgift): test 3
Ok, lade till "test 3" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Klarmarkerade uppgifter:
0: test 4

Skriv in en ny sak du måste komma ihåg att göra (använd nummer för att välja gammal uppgift): 0
Ok, lade till "test 4" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra (använd nummer för att välja gammal uppgift): fika
Ok, lade till "fika" i listan
.
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
quit. Avsluta
Välj ett alternativ: quit
Avslutar programmet
```