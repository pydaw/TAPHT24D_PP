  
# Uppgift 1
  
### Läsa och förstå kod - diskutera i grupp
Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?

**1a**
```python
def foo(t):
    print("test")
  
foo("hej")`
```
  
**1b**
```python
def fun1(x, y):
    return x * y
  
print(3, 5)`
```
  
**1c**
```python
def fun1(x, y):
    return x * y

print(fun1(3, 5))`
```
  
**1d**
```python
def fun2(i):
    return 5 * i
  
x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)`
```
  
**1e**
```python
a = 5
def fun3(a):
    a += 1
  
a += 2
print(a)`
```
  
**1f**
```python
def foo(i):
    return 2*i*i
  
def goo(x, y):
    return x(y)
  
a = goo(foo, 3);
print(a)
```
  
**1g** 
Funktionen "isinstance" kan kontrollera en variabels datatyp. Vad gör funktionen is_number? Går det att förbättra koden?
```python
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
```
  
**1h**
```python
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found
  
average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
```
  
**1i** 
En uppgift i tre delar:
Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
Rätta felen, så funktionen gör det den ska.
  
```python
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
  
# Alternativ 1
def find_min(numbers):
    counter = None
    for item in numbers:
	 if counter is None
	     counter = item
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter
  
find_min([10, 3, -4, -11])
find_min([])
find_min([100])
```
  
  
### Reflektioner
  
| #   | Förväntat resultat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1a  | Skriver ut "test" eftersom parameter t inte används i koden                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 1b  | Kommer att skriva ut "3" o "5", eftersom man inte anropar den tilltänkta funktionen                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 1c  | Borde skiva ut 15 eftersom den anropar funktionen                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 1d  | Borde bli 125, eftersom den anropar en funktion som gångar med 5. Funktionen anropas nästat vilket blir:<br>fun2(fun2(x) + fun2(y)) = 5(5x2+5x3) = 5x25 = 125                                                                                                                                                                                                                                                                                                                                                |
| 1e  | Borde skriva 7, eftersom funktionen inte anropas                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 1f  | Borde bli 18, eftersom man skickar in funktionen foo i goo med argumentet 3. Vilket då blir 2x3x3 = 18                                                                                                                                                                                                                                                                                                                                                                                                       |
| 1g  | is_number tar reda på att om argumentet är nummeriskt. Det räcket att kolla om man gör om den till en float kan man kolla om den är nummerisk med mindre antal rader. Annars tycker jag det verkar som en bra lösning. isinstance kan även skrivas på en rad med or villkor eller en tuple.                                                                                                                                                                                                                  |
| 1h  | Returerar orden mellan 4 o 8 bokstäver                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 1i  | Funktionen går ut på att hitta minsta värdet på en lista som man skickar in. <br><br>Men den verka inte fungera så bra eftersom om man skickar in en tom lista eller bara ett värde kommer variablen counter vara noll och därmed redan vara det minsta värdet. dvs kommer counter retuneras. Där av kommer en lista med värden som är över noll att bara returnera 0.<br><br>Alternativ lösning är att man sätter counter till None och kontrollera att om None förekommer så sätter man counter till item. |
  
# Uppgift 2
  
1 Skriv en funktion som tar en sträng som parameter. När den anropas ska den skriva ut strängen och "är en fena på programmering". Exempel:
my_function("David") → "David är en riktig hacker"
  
Lösning:
Tar in parameter username som man sedan lägger till i början av meddelandet som man printar ut.
  
Testfall:
```log
my_module1.my_function("David") -->
David är en riktig hacker
  
my_module1.my_function("Daniel") -->
Daniel är en riktig hacker
```
  
  
2a Skriv en funktion med namnet "eko". När den anropas med en sträng ska den upprepa strängen, och skriva ut resultatet. Exempel:
eko("hej") → skriver ut "hejhej"
  
Lösning:
Tar parametern som innehåller ekomeddelandet och multiplicerar med värdet i parameter count som är satt till default 2.
  
Testfall:
```log
my_module2.eko("hej") -->
hejhej
```
  
  
2b Lägg till en parameter "count", som avgör hur många ekon som ska skapas. Exempel:
eko("hej", 3) → skriver ut "hejhejhej"
  
Lösning:
Tar parametern som innehåller ekomeddelandet och multiplicerar med värdet i parameter count.
  
Testfall:
```log
my_module2.eko("hej", 3) -->
hejhejhej
```
  
  
3 Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion och justera den enligt kommentaren.
```python
end = 5
y = 1
for x in range(1, 100):
    y *= 2
    # avsluta loopen med en if-sats här
print(y)
```
  
Lösning:
if satsen använder variabeln end som den jämför med x. Om x och end är samma så kan man anropa break för att avsluta loopen.
Debug genom att sätta print(y) eller print(x) i for loopen för att se hur många ggr den skrivs ut. Alternativt att man sätter en breakpoint i loopen för att se hur många ggr loopen körs.
  
Testfall:
```log
# Test med debug o print(x) i for loopen:
1
2
3
4
5
32
  
# Utan debug utskrift:
32
```
  
  
4 Skriv en funktion med namnet last. Den ska ta en lista som parameter och returnera det sista elementet i listan.
last([1, 2, 3]) → 3
  
Lösning:
Använder slice på listan för att bara ta sista elementet:
```python
def last(last_list):
    return last_list[-1]
```
  
Testfall:
```log
print(my_module4.last([1, 2, 3])) --> 3
print(my_module4.last([1, 2])) --> 2
print(my_module4.last([1])) --> 1
print(my_module4.last([])) --> Traceback
```
  
  
5 Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.
cut_edges([1, 2, 3, 4]) → [2, 3]
  
Lösning:
Använder slice och returnerar index mellan 1 till -1...dvs det andra o det näst sitsa indexet. Kastar även ett exception om man har för få element i listan.
  
```python
def cut_edges(input_list):
    if len(input_list)>=2:
        return input_list[1:-1]
    else:
        raise Exception("List need two elements or more")
```
  
  
Testfall:
```log
print(my_module5.cut_edges([1, 2, 3, 4])) --> [2, 3]
print(my_module5.cut_edges([1, 2, 3])) --> [2]
print(my_module5.cut_edges([1, 2])) --> []
print(my_module5.cut_edges([1])) -->
  
Traceback (most recent call last):
  File "c:\Users\dawa01\Documents\Python Scripts\nbi\TAPHT24D_PP\Veckouppgift 4\uppgift2\main.py", line 58, in <module>
    print(my_module5.cut_edges([1]))
  File "c:\Users\dawa01\Documents\Python Scripts\nbi\TAPHT24D_PP\Veckouppgift 4\uppgift2\my_module5.py", line 6, in cut_edges
    raise Exception("List need two elements or more")
Exception: List need two elements or more
```
  
  
6 Lös felen i koden.
```python
def increase(x):
    return x
    x += 1
  
print(increase(1))
```
  
Lösning:
Return kommandot gör så att inte underliggande kod körs. Genom att flytta ned return under "x += 1" så kan funktionen köras. 
  
Testfall:
```log
print(my_module6.increase(1)) --> 2
```
  
  
7 Bygg en funktion med namnet average. Den ska ta parametrar: x och y. Båda ska vara tal. Funktionen ska returnera medelvärdet. Till exempel så räknar man ut medelvärdet av 4 och 8 genom med formeln: (4 + 8) / 2, vilket blir 6.
Tips: det kan vara enklare att använda fler variabler.
  
Lösning:
Kollar först om parametrarna x och y är nummer. Detta tas reda på med en separat funktion. Om inte dessa parametrar är nummer så kastas ett exception ut som meddelar att man måste ha nummer som argument.
  
Om x och y är nummer beräknas medelvärdet och returneras.
  
Testfall:
```log
print(my_module7.average(4,8)) --> 6.0
print(my_module7.average("a","b")) --> Exception: Argument is not a number
print(my_module7.average("a",8)) --> Exception: Argument is not a number
print(my_module7.average(4,"b")) --> Exception: Argument is not a number
```
  
  
8 Gör en funktion som kan skriva ut innehållet i en lista lite snyggare. Först ska funktionen tala om ifall listan är tom, eller hur många element den har. Sedan ska funktionen skriva ut elementen i en punktlista. 
Exempel:
´pretty_print(["a", "b", 3.14])´
Listan har 3 element:
1. a
2. b
3. 3.14
  
Lösning:
Kontrollerar om listan har element, har den element skrivs hur många element listan har. Punktlistan görs med en for loop som loopar igenom listan och printar ut varje element med en f string. Index tas reda på med index funktionen. indexet adderas med 1 för att listans index skall börja på 1.
  
Testfall:
```log
my_module8.pretty_print([]) -->
Listan är tom
  
my_module8.pretty_print(["a", "b", 3.14]) -->
Listan har 3 element:
1: a
2: b
3: 3.14
```
  
  
# Uppgift - Spelet 21 
  
Om man lägger ihop talen 1 + 2 + 3 + 4 + …  så kommer talens summa att bli större och större. Förr eller senare kommer man förbi 21. Skriv en funktion som skriver ut det första talet i talserien som är större än 21.
    
Version 2: i stället för att använda talserien, slumpa tal mellan 1 och 13. (talen i en vanlig kortlek)
Tips: importera modulen random och använd funktionen randint för att slumpa tal. 
Exempel: card = random.randint(1, 13)
  
Möjlig vidareutveckling: bygg ett spel som frågar användaren om man vill ta ett nytt kort eller stanna. (slumpa ett tal) Gör så att datorn kan simulera en motståndare. Målet är att vinna över datorn.

Lösning:
Version 1 -  Gjort en funktion som loopar igenom talen 1 till  21 och summerar dessa. Om summas blir större än 21 så stannar loopen och rapporterar vilket nummer loopen stannade på samt vilken summa. funktionen returnerar summan.
  
Version2 - Gör om funktionen så att  en loop körs  21 ggr (dvs om det skulle bli massor av ettor. Ett slumpvist kort slumpas fram och summeras till en summa samt skrivs ut. Om summan är större än 21 skrivs värde på kort ut samt summan.
Summan returneras.
  
Version3 - Döper om funktionen till new_card. Funktionen görs om till att slumpmässigt ta fram ett kort och skriva ut kortet som slumpats fram och om kortet gjort så att man kommer över 21. Även lagt till logik för att spela  21 mot en simulerad spelare. Båda spelarna kan välja att fortsätta eller att stanna. I slutet finns även logik för att ta fram vem som vunnit spelet.
  
Testfall:
```log
===== Kort omgång: 1 =====
--- Spelare1 ---
Dim summa är: 0
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: ja
Slumpmässigt kort: 12
  
--- Spelare2 (Dator) ---
Dim summa är: 0
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Ja
Slumpmässigt kort: 8
  
===== Kort omgång: 2 =====
--- Spelare1 ---
Dim summa är: 12
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: ja
Slumpmässigt kort: 5
  
--- Spelare2 (Dator) ---
Dim summa är: 8
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Ja
Slumpmässigt kort: 9
  
===== Kort omgång: 3 =====
--- Spelare1 ---
Dim summa är: 17
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: nej
Spelare 1 har stoppat på summan: 17
  
--- Spelare2 (Dator) ---
Dim summa är: 17
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Nej
Spelare 2 har stoppat på summan: 17
  
Ingen har vunnit oavgjort!
  
  
  
  
  
===== Kort omgång: 1 =====
--- Spelare1 ---
Dim summa är: 0
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: ja
Slumpmässigt kort: 1
  
--- Spelare2 (Dator) ---
Dim summa är: 0
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Ja
Slumpmässigt kort: 4
  
===== Kort omgång: 2 =====
--- Spelare1 ---
Dim summa är: 1
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: ja
Slumpmässigt kort: 10
  
--- Spelare2 (Dator) ---
Dim summa är: 4
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Ja
Slumpmässigt kort: 11
  
===== Kort omgång: 3 =====
--- Spelare1 ---
Dim summa är: 11
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: ja
Slumpmässigt kort: 8
  
--- Spelare2 (Dator) ---
Dim summa är: 15
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Nej
Spelare 2 har stoppat på summan: 15
  
===== Kort omgång: 4 =====
--- Spelare1 ---
Dim summa är: 19
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: nej
Spelare 1 har stoppat på summan: 19
  
Spelare 1 har vunnit!
  
  
  
  
  
===== Kort omgång: 1 =====
--- Spelare1 ---
Dim summa är: 0
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: ja
Slumpmässigt kort: 6
  
--- Spelare2 (Dator) ---
Dim summa är: 0
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Ja
Slumpmässigt kort: 5
  
===== Kort omgång: 2 =====
--- Spelare1 ---
Dim summa är: 6
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: ja
Slumpmässigt kort: 12
  
--- Spelare2 (Dator) ---
Dim summa är: 5
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Ja
Slumpmässigt kort: 8
  
===== Kort omgång: 3 =====
--- Spelare1 ---
Dim summa är: 18
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: ja
Slumpmässigt kort: 10
Kort '10', summa är'28' > 21
  
--- Spelare2 (Dator) ---
Dim summa är: 13
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Ja
Slumpmässigt kort: 9
Kort '9', summa är'22' > 21
  
Ingen har vunnit båda är över 21!
  
  
  
  
===== Kort omgång: 1 =====
--- Spelare1 ---
Dim summa är: 0
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: ja
Slumpmässigt kort: 12
  
--- Spelare2 (Dator) ---
Dim summa är: 0
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Ja
Slumpmässigt kort: 12
  
===== Kort omgång: 2 =====
--- Spelare1 ---
Dim summa är: 12
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: ja
Slumpmässigt kort: 4
  
--- Spelare2 (Dator) ---
Dim summa är: 12
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Ja
Slumpmässigt kort: 3
  
===== Kort omgång: 3 =====
--- Spelare1 ---
Dim summa är: 16
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: ja
Slumpmässigt kort: 7
Kort '7', summa är'23' > 21
  
--- Spelare2 (Dator) ---
Dim summa är: 15
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Nej
Spelare 2 har stoppat på summan: 15
  
===== Kort omgång: 4 =====
--- Spelare1 ---
Dim summa är: 23
Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: nej
Spelare 1 har stoppat på summan: 23
  
Spelare 2 har vunnit!
  
```
  
  
  
# Uppgift - Pokerhand
  
När man spelar poker har man en hand med 5 kort, som man hoppas ska bli bättre än motståndarnas. Du ska bygga en funktion som kan utvärdera en pokerhand och tala om hur bra den är. 
Exempel på körning:
poker_hand(cards)
"Du fick ett par med valören: 5"
  
  
1 Bygg en funktion som slumpar ett spelkort. Den ska returnera en lista med två element: färg och valör. Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess, för enkelhets skull använder vi talen 2 till 14.
Exempel på ett kort: ["hjärter", 12]
  
Testfall:
```python
def get_random_card():
    colors = [ "hjärter", "spader", "ruter", "klöver"]
    value = [i for i in range(2,14+1)]
    print(value)
    return [choice(colors), choice(value)]
  
card = get_random_card()
print(f"Kort: {card}")
```
  
```log
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
Kort: ['hjärter', 14]
  
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
Kort: ['klöver', 10]
```
  
   
2 Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.
  
Testfall:
```python
card1 = get_random_card()
card2 = get_random_card()
  
  
print(f"Kort1: {card1}, Kort2: {card2}")
print(f"Är kortens värde lika?: {is_card_value_equal(card1, card2)}")
```
  
```log
#### Test av 1 och 2: ####
Kort1: ['hjärter', 5], Kort2: ['spader', 5]
Är kortens värde lika?: True
  
  
Kort1: ['hjärter', 3], Kort2: ['ruter', 8]
Är kortens värde lika?: False
```
  
  
3 Bygg första versionen av poker_hand(cards). Med hjälp av de andra funktionerna ska den ta reda på om man har ett par, dvs det finns två kort med samma valör.
  
  
Fortsätt att lägga till fler kontroller till funktionen.
Tips! Du kan göra en funktion som skriver ut kortvärdet snyggare:
pretty_print_card(["hjärter", 5]) → "hjärter fem"
  
Lista med pokerhänder.
- Ett par (två lika kort)
- Två par
- Tretal (tre lika)
- Straight (5 kort i följd, t.ex. 7-8-9-10-11)
- Flush / färg (alla kort har samma färg)
- Hus (par och tretal med olika valörer)
- Fyrtal
- Straight flush (5 kort i följd, med samma färg)
- Femtal
  
  
Testfall:
Observera att femtal är implenterad i koden men går inte att få eftersom man bara har 4 färger.

```log
#### Test av pokehand: ####
Aktuell pokerhand: spader fem, spader tio, ruter två, ruter tre, klöver ess
Du fick inte så bra pokerhand!
  
Aktuell pokerhand: hjärter tre, klöver fem, spader två, ruter tre, klöver åtta
Du fick 'Par' med valören 'tre'
  
Aktuell pokerhand: spader tre, klöver sex, ruter fyra, spader sex, spader fyra
Du fick 'Par' med valören 'sex'
Du fick 'Par' med valören 'fyra'
Du fick 'Två par'
  
Aktuell pokerhand: klöver två, spader tio, spader två, hjärter två, ruter sju
Du fick 'Tretal' med valören 'två'
  
Aktuell pokerhand: ruter knekt, spader knekt, hjärter knekt, klöver knekt, hjärter åtta
Du fick 'Fyrtal' med valören 'knekt'
  
Aktuell pokerhand: ruter knekt, spader knekt, hjärter knekt, klöver åtta, hjärter åtta
Du fick 'Tretal' med valören 'knekt'
Du fick 'Par' med valören 'åtta'
Du fick 'Hus'
  
Aktuell pokerhand: hjärter ess, spader knekt, hjärter kung, klöver dam, hjärter tio
Du fick 'Straight'
  
Aktuell pokerhand: hjärter ess, hjärter knekt, hjärter tre, hjärter dam, hjärter tio
Du fick 'Flush'
  
Aktuell pokerhand: hjärter ess, hjärter knekt, hjärter kung, hjärter dam, hjärter tio
Du fick 'Straight Flush'
  
```
  
# Uppgift 5 - Turtle graphics
  
Python har ett paket med inbyggda, enkla funktioner för grafik: turtle. Tänk dig att du har en robotarm som håller en penna mot ett papper. Man kan ge olika instruktioner till roboten, för att styra den. Några exempel:
forward - gå rakt framåt i standardriktningen (peka ursprungligen åt höger)
backward - gå bakåt
left, right - sväng vänster eller höger ett antal grader, 360 grader för ett helt varv
dot - sätt ut en prick med en viss storlek
speed - normal=6, fast=10, maximal=0
  
Läs mer här: Turtle graphics — Python 3.13.1 documentation 
Kodexempel:
```python
import turtle as t
  
# Upprepa 3 gånger
for x in range(3):
    t.forward(100)
    t.left(120)
  
# Lyft pennan för att flytta utan att rita
t.penup()
t.forward(200)
t.pendown()
t.dot(10, "red")
t.color("blue"
t.forward(50)
  
# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()
```
  
  
1 Skriv en funktion som ritar en kvadrat. Längden på sidan ska vara en parameter till funktionen.
  
Kod:
```python
import turtle as t
  
# funktion som ritar en kvadrat, default längd på sida är 100px
def sqare(side=100):
    for i in range(4):
        t.forward(side)
        t.left(90)
  
  
# Ritar en kvadrat med en sida på 100px
sqare(100)
  
# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()
```
  
Testfall:  
![Pasted image 20250129153735.png](https://github.com/pydaw/TAPHT24D_PP/blob/main/Veckouppgift%204/img/Pasted%20image%2020250129153735.png)
  
2 Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita. Tanken är att du ska kunna kombinera den med kvadratfunktionen, för att rita flera kvadrater. Exempel:
for x in range(5):
    t.square()
    t.move_next()
  
Kod:
```python
import turtle as t
  
# funktion som ritar en kvadrat
def square(side=50):
    for i in range(4):
        t.forward(side)
        t.left(90)
  
# funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita
def move_next(distance=100):
    t.penup()
    t.forward(distance)
    t.pendown()
  
  
# Ritar 5 kvadrater 
for x in range(5):
    square()
    move_next()
  
# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()
```
  
Testfall:  
![Pasted image 20250129154743.png](https://github.com/pydaw/TAPHT24D_PP/blob/main/Veckouppgift%204/img/Pasted%20image%2020250129154743.png)
  
  
3 Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel. Använd parametrar i stället för värdena 7, 40 och 30.
Tips 1: vad händer om man varierar värdet på range? 
Tips 2: 360 grader motsvarar ett helt varv.
for x in range(7):
    t.forward(40)
    t.right(30)
  
  
Lösning:
Om man ökar range antalet dvs. kör flera loopar måste man minska antalet grader på att svänga höger. 
Parameterna  'loop' multiplicerat med 'right_angle' skall bli 360°.
  
Har minskat right_angle och ökat loops parametern så att det skall se ut som en cirkel.
  
Har även minskar forward parametern så det slipper bli så stora cirklar.
  
  
Kod:
```python
import turtle as t
  
def move(loops, forward, right_angle):
    for x in range(loops):
        t.forward(forward)
        t.right(right_angle)
  
def circle(size):
    move(loops=360,forward=size/100.0,right_angle=1)
  
  
# Ritar en cirkel
circle(100)
  
# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()
```
  
Testfall:  
![Pasted image 20250129161210.png](https://github.com/pydaw/TAPHT24D_PP/blob/main/Veckouppgift%204/img/Pasted%20image%2020250129161210.png)
  
  
4 Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med turtle-modulen. Kombinera dem och försök få bokstäverna att ritas med samma storlek, på en rak linje.
  
Kod:
```python
import turtle as t
import math
  
__version__ = 2
  
if __version__ == 1:
    t.write('PYTHON' , font=('Arial', 35, 'normal'))
  
    # Låt fönstret stanna kvar tills användaren stänger det
    t.mainloop()
  
elif __version__ == 2:
    def calc_angle_distance(a,b):
        return math.sqrt(a**2+b**2)

    def calc_angle(angle_distance, x_offset):
        return math.degrees(math.asin(x_offset/angle_distance))
      
  
  
    # funktion som ritar bokstaven "P"
    def letter_p():
        t.setheading(0)
        t.left(90)
        t.forward(170)
        t.right(90)
        t.forward(20)
        t.circle(-50,180)
        t.forward(20)
      
  
    # funktion som ritar bokstaven "Y"
    def letter_y():
        t.setheading(0)
        t.left(90)
        height = 170
        t.forward(height*0.6)
        angle_distance = calc_angle_distance(height-height*0.6,height/3)
        angle = calc_angle(angle_distance, height/3)
        t.left(angle)
        t.forward(angle_distance)
        t.penup()
        t.backward(angle_distance)
        t.pendown()
        t.right(angle*2)
        t.forward(angle_distance)
  
  
    # funktion som ritar bokstaven "T"
    def letter_t():
        t.setheading(0)
        t.left(90)
        t.forward(170)
        t.left(90)
        t.forward(60)
        t.left(180)
        t.forward(120)
        
  
    # funktion som ritar bokstaven "H"
    def letter_h():
        t.setheading(0)
        t.left(90)
        t.forward(170)
        t.penup()
        t.backward(85)
        t.pendown()
        t.right(90)
        t.forward(85)
        t.left(90)
        t.penup()
        t.forward(85)        
        t.pendown()
        t.right(180)
        t.forward(170)
  
  
    # funktion som ritar bokstaven "O"
    def letter_o():
        t.setheading(0)
        t.left(180)
        t.circle(-50,90)
        t.forward(70)
        t.circle(-50,180)
        t.forward(70)     
        t.circle(-50,90)
  
  
    # funktion som ritar bokstaven "N"
    def letter_n():
        t.setheading(0)
        t.left(90)
        t.forward(170)
        angle_distance = calc_angle_distance(170,85)
        angle = calc_angle(angle_distance, 85)
        t.right(180-angle)
        t.forward(angle_distance)
        t.left(180-angle)
        t.forward(170)
  
      
    # funktion som flyttar pennan lämplig punkt, utan att rita
    def bring_to_point(x=-400, y=0, x_offset=0, y_offset=0):
        t.penup()
        t.setheading(0)
        t.setpos(x + x_offset, y + y_offset)
        t.pendown()
          
    
    t.speed('fastest')
    bring_to_point()
    letter_p()
    bring_to_point(x_offset=120)
    letter_y()
    bring_to_point(x_offset=250)
    letter_t()
    bring_to_point(x_offset=320)
    letter_h()
    bring_to_point(x_offset=468)
    letter_o()
    bring_to_point(x_offset=530)
    letter_n()
    
  
    # Låt fönstret stanna kvar tills användaren stänger det
    t.mainloop()
```
  
Testfall:  
   
Version1:  
![Pasted image 20250130102051.png](https://github.com/pydaw/TAPHT24D_PP/blob/main/Veckouppgift%204/img/Pasted%20image%2020250130102051.png)
  
Version2:  
![Pasted image 20250130102026.png](https://github.com/pydaw/TAPHT24D_PP/blob/main/Veckouppgift%204/img/Pasted%20image%2020250130102026.png)
  
  
Bonusuppgift, lär dig rekursiva funktioner med turtle graphics:
Python Turtle Meets Fractal Art: A Recursive Journey 
  
Kod:
```python
import turtle as t
  
def get_mid(p1, p2):
    return ((p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2)
  
def draw_triangle(t, vertices, color):
    t.fillcolor(color)
    t.up()
    t.goto(vertices[0][0], vertices[0][1])
    t.down()
    t.begin_fill()
    t.goto(vertices[1][0], vertices[1][1])
    t.goto(vertices[2][0], vertices[2][1])
    t.goto(vertices[0][0], vertices[0][1])
    t.end_fill()
  
def draw_sierpinski(t, vertices, depth):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    color = depth % len(colormap)
    draw_triangle(t, vertices, colormap[color])
    if depth > 0:
        draw_sierpinski(t, [vertices[0],
                            get_mid(vertices[0], vertices[1]),
                            get_mid(vertices[0], vertices[2])],
                       depth - 1)
        draw_sierpinski(t, [vertices[1],
                            get_mid(vertices[0], vertices[1]),
                            get_mid(vertices[1], vertices[2])],
                       depth - 1)
        draw_sierpinski(t, [vertices[2],
                            get_mid(vertices[2], vertices[1]),
                            get_mid(vertices[0], vertices[2])],
                       depth - 1)

  
# Set up the drawing canvas
t.setup(800, 600)
window = t.Screen()
window.bgcolor("white")
window.title("Sierpinski Triangle")
  
# Creating the Turtle to draw the triangle
sierpinski = t.Turtle()
sierpinski.speed('fastest')
  
points = [[-200, -100], [0, 200], [200, -100]]  # Define the main triangle points
draw_sierpinski(sierpinski, points, 5)  # Change the depth as needed
  
t.done()
```
  
Testfall:  
![Pasted image 20250130102257.png](https://github.com/pydaw/TAPHT24D_PP/blob/main/Veckouppgift%204/img/Pasted%20image%2020250130102257.png)
  