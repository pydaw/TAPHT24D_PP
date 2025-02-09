# Uppgift 1 - Läsa och förstå kod - diskutera i grupp
Skriv ner vad du tror kommer skrivas ut. 
Skriv sedan in koden i din IDE, exakt som den står, och kör den. 
Fick du samma resultat som du trodde? Om inte, varför?
  
  
> [!INFO]  Ekvivalentklasser inom mjukvarutestning
>
>Inom **testning** används ekvivalentklasser för att dela in möjliga indata i grupper där varje grupp antas ge samma resultat vid testning. 
>Syftet är att minska antalet testfall utan att förlora testtäckning.
>
>- **Exempel:** Om en funktion tar emot en ålder som input och endast accepterar personer mellan 18 och 65 år kan ekvivalentklasserna vara:
  >  - **Giltiga värden:** 18–65
  >  - **Ogiltiga värden:** <18 och >65
  >  - Istället för att testa varje enskilt tal testar man representativa värden från varje klass (t.ex. 17, 18, 30, 65, 66).
  
  
1 Vilka ekvivalensklasser har uttrycken?
1a. 
x > 100
  
Villkoret blir True om 'x': Är en int eller float som är strikt större än 1000
Villkoret blir False om 'x': Är int eller float som är lika med 100 eller mindre. Samt om 'x' är en boolean. 
  
  
1b.
y == 42
  
Villkoret blir True om 'y:' Är int eller float som är lika med 42
Villkoret blir False om 'y:' Är int eller float som inte är lika 42, samt alla andra domäner.
  
  
1c. 
len(text) >= 5
  
Villkoret blir True om 'text': Är en sekventiell domän som har längden 5 eller längre.
Villkoret blir False om 'text': Är sekventiell domän som en längd som är strikt under 5.
  
  
1d. 
z == True
  
Villkoret blir Trure om 'z': Är boolean eller boolerskt uttryck som är lika med True.
Villkoret blir False om 'z': Är boolean eller boolerskt uttryckt som är lika med värdet False, samt all andra domäner.
  
  
1e.
8 < v < 16
  
Villkoret blir Trure om 'v':  Är int eller float som är strikt större än 8 samt strikt mindre än 16.
Villkoret blir False om 'v:  Är int eller float som är lika med 8 eller mindre eller 16 eller större. Booleska uttryck och boolean ger också False.
  
  
1f. 
w == 32 or w == 64 or w == 128
  
Villkoret blir True om 'w': Är lika med int eller float som antar värdena 32, 64 eller 128.
Vilkoret blir False om 'w': Är andra int eller float värden, eller tillhör en annan domän.
  
  
1g. 
if x < 5: … elif x < 10: … elif x < 15: … else
  
Villkoret för x < 5 blir True om 'x' är: Int eller float som är strikt mindre än 5, samt om variabeln är en boolean.
Villkoret för x < 10 blir True om 'x' är: Int eller float som är lika med 5 eller större ock strikt mindre än 10.
Villkoret för x < 15 blir True om 'x' är: Int eller float som är lika med 10 eller större och strikt mindre än 15. 
Villkoret för att komma till else är: Int eller float som är lika med 15 eller större. 
  
  
2 Det har smugit sig in kommentarer i stället för kod på några ställen. Skriv färdigt testfallen test_empty_list och test_number_list.
```python
# Returnerar summan av alla tal i listan
def sum_list(list):
    return None

def test_empty_list():
    expected = # ???
    actual   = # 
    assert actual == expected
    
def test_number_list():
    assert sum_list([5]) == 5
    assert # ???
    assert # ???
    assert # ???
```
  
Lösning 
```python
# Returnerar summan av alla tal i listan
def sum_list(list):
    return None

def test_empty_list():
    expected = 0
    actual   = sum_list([]) 
    assert actual == expected
    
def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([1,2,3,4,5]) == 15
    assert sum_list([0,0,0,0,0]) == 0
    assert sum_list([-1,-2,-3,-4,-5]) == -15
```
  
  
3a Diskutera följande kod. Räcker det med ett testfall för att testa funktionen?
```python
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
def count_vowels(word):
    return None

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0
```
  
Själva testerna i sig dvs assert kommandona ser bra ut men kana delas upp i olika tester,
för att förhindra att något test fallerar så syns inte hur de andra assert testerna gick.
  
  
3b Skriv färdigt funktionen count_vowels med hjälp av TDD-metoden, red → green → refactor.
  
Lösning:
```python
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
def count_vowels(word):
    return 0
  
def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0
```
  
Här så returnerar vi 0 då kommer testet att gå igenom. Man får sedan skriva mer tester för att skriva färdigt funktionen med rätt innehåll.
  
  
4 Formulera testfall för en funktion som hittar största talet i en lista.
```python
# Returnerar det största talet i listan
# Returnerar None om det inte finns något
def find_max(list):
```
  
Lösning:
```python
# Returnerar det största talet i listan
# Returnerar None om det inte finns något
def find_max(list):
	return None


def test_greatest_number_in_list():
    excepted = 80
    actual = find_max([60, 30, 80, 1])

    assert actual == excepted


def test_greatest_number_in_list_is_none_when_list_is_empty():
    excepted = None
    actual = find_max([])

    assert actual == excepted
```
  
  
5 Winner takes it all brukar det ju heta, men nu ska vi försöka ge lite heder åt alla andrapristagare. Formulera testfall för en funktion som hittar näst största talet i en lista!
```python
# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet
def find_2nd_max(list):
```
  
Lösning:
```python
def find_2nd_max(list):
    None
  
  
def test_2nd_greatest_number_in_list():
    excepted = 60
    actual = find_2nd_max([60, 30, 80, 1])

    assert actual == excepted
  
  
def test_2nd_greatest_number_in_list_is_none_when_list_is_empty():
    excepted = None
    actual = find_2nd_max([])

    assert actual == excepted
```
  
  
# Uppgift 2 - Öva på TDD
Samla ihop dina funktioner så att de ligger i en eller flera moduler. Importera och anropa dem från main.py, så att main-filen bara innehåller funktionsanrop.
  
1a Hitta på lämplig testdata till följande funktion, som omvandlar grader Celsius till grader Fahrenheit.
```python
def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32
```
  
 Förslag på värden att testa med:
  
| ° Celsius  | ° Fahrenheit | Kommentar                                                               |
| ---------- | ------------ | ----------------------------------------------------------------------- |
| 0          | 32           |                                                                         |
| -17.777... | 0            |                                                                         |
| 37.777...  | 100          |                                                                         |
| 100        | 212          |                                                                         |
| True       | 33.8         | Hade det varit bättre att inte stödja denna domän, dvs returnea 'None'  |
| False      | 32           | Hade det varit bättre att inte stödja denna domän, dvs returnera 'None' |
| -273.1     | None         |                                                                         |
  
1b Vilka ekvivalensklasser har parametern degree?
  
Villkoret blir True om 'degree': Är en in eller float och är strikt mindre än -273.15.
Villkoret blir False om 'degree': Är en in eller float och är lika med -273.15 eller större än. Kan också vara en boolean.
  
  
1c Skriv ett testfall.
  
Lösning:
```python
def test_convert_celcius_to_fahrenheit():
  
# | ° Celsius  | ° Fahrenheit |
# | ---------- | ------------ |
# | 0          | 32           |
# | -17.777... | 0            |
# | 37.777...  | 100          |
# | 100        | 212          |
# | True       | 33.8         |
# | False      | 32           |
# | -273.1     | None         |
  
    assert module.c_to_f(0) == 32
    assert module.c_to_f(-17.777) == approx(0, abs=1e-2)
    assert module.c_to_f(37.777) == approx(100, abs=1e-2) 
    assert module.c_to_f(100) == 212
    assert module.c_to_f(True) == 33.8
    assert module.c_to_f(False) == 32
    assert module.c_to_f(-273.151) is None
```
  
```log
.                                                                        [100%]
1 passed in 0.01s
Finished running tests!
```
  
  
2a Betrakta funktionen count_words(sentence), som tar en sträng och returnerar antalet ord. Ett ord är en serie tecken som separeras av mellanslag. 
Formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.
  
AK:
- Indata skall vara en sträng
- Utdata skall vara en integer som inte kan vara negativ
- Funktionen skall seprarera ord i strängen genom mellanslag (kan vara flera mellanslag)
- Om indata inte är en sträng skall funktion returnera None
  
  
2b Skriv testfall som testar alla AK.
  
Lösning:
```python
def test_count_words():
    assert test_count_words("Hej hopp i lingonskogen!") == 4
    assert test_count_words("Hej!") == 1
    assert test_count_words("Hej        hopp i lingonskogen!") == 4
    assert test_count_words("") == 0
    assert test_count_words(["Hej","på","dej!"]) is None
    assert test_count_words(True) is None
    assert test_count_words(32) is None
```
  
2c Implementera funktionen, så att alla testfall blir gröna.
  
Lösning:
```python
def count_words(sentence):
    if isinstance(sentence, str):
        return len(sentence.split())
    else:
        return None
```
  
```log
.                                                                        [100%]
1 passed in 0.02s
Finished running tests!
```
  
  
3a Betrakta funktionen `find_median(numbers)`, som tar en lista med tal och returnerar medianen. 
Median är det mittersta talet, t.ex. är medianen `2` för listan `[1, 2, 1000]`. 
Om listan har jämnt antal element ska funktionen returnera medelvärdet av de två mittersta talen. 
Formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.
  
AK:
- Funktionens indata skall bestå av en lista vars element består av tall (float eller integer). Om listan består av annan domän skall funktionen returnera 'None'
- Ojämnt antal element i listan skall det mittersta elementet returneras
- Jämnt antal element i listan skall medelvärdet på det två mittersta elementen returneras
- Tom lista returneras 'None'
  
3b Skriv testfall som testar alla AK.
  
Lösning:
```python
def test_find_median():
    assert module.find_median([1,2,1000]) == 2
    assert module.find_median([1,100,100,1000]) == 100
    assert module.find_median([1.0,2.0,1000.0]) == 2.0
    assert module.find_median([1]) ==1
    assert module.find_median([]) is None
    assert module.find_median([1,True,"str"]) is None
    assert module.find_median("1234") is None
    assert module.find_median(1234) is None
    assert module.find_median(True) is None
```
  
```log

```
  
  
3c Implementera funktionen, så att alla testfall blir gröna.
'Lösning:
```python
def find_median(numbers):
    # Check if numbers is a list
    if not isinstance(numbers, list):
        return None
    
    # Check if list is not empty
    numbers_length = len(numbers)
    if not numbers_length > 0:
        return None

    # Check if numbers is made of 
    for element in numbers:
        if not isinstance(element,(int,float)):
            return None
    
    # Sort list
    numbers.sort()

    # Odd number of elements 
    if numbers_length % 2 == 1:
        index = int((numbers_length-1)/2)
        return numbers[index]

    # Even number of elements
    else:
        index1 = int(numbers_length/2-1)
        index2 = int(numbers_length/2)
        return (numbers[index1] + numbers[index2])/2
```
  
```log
.                                                                        [100%]
1 passed in 0.01s
Finished running tests!
```
  
  
4 Betrakta funktionen `is_sorted_ascending(numbers)`. 
Den ska returnera `True` om listan numbers är sorterad i stigande ordning, `False` annars.
  
4a Vilka ekvivalensklasser har numbers?
  
Giltliga väden för numbers: lista med  > 0 antal element samt med tal som är sorterade i stigande ordning.
Ogiltliga värden för numbers: Osorterade listor, eller om numbers innehåller annan domän än en sorterad lista. 
  
  
4b Formulera krav och acceptanskriterier för funktionen.
  
AK:
- numbers skall vara av domänen lista
- numbers alla element skall vara av domänen int eller float
- Funktionen skall returnera True om numbers är sorterad med stigande tal
- Funktionen skall returnera False om inte ovanstående kriterier är uppfyllda
  
  
4c Skriv testfall för funktionen.
  
```python
def test_is_is_sorted_ascending():
    assert module.is_sorted_ascending([1,2,1000]) == True
    assert module.is_sorted_ascending([1,1000,2]) == False
    assert module.is_sorted_ascending([1,2,"str"]) == False
    assert module.is_sorted_ascending([]) == False
    assert module.is_sorted_ascending(True) == False
    assert module.is_sorted_ascending(123) == False
    assert module.is_sorted_ascending("str") == False
```
  
# Uppgift 3 - Söka efter användare
Tänk dig en funktion som kan användas för att visa sökresultat medan användaren skriver i ett sökfält. Funktionen ska ta två parametrar: input är det användaren skriver, master_list är en lista med alternativ som kan hittas.
```python
def autocomplete_list(input, master_list):
```
  
Börja med att formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.
Välj sedan ut ett AK och skriv ett testfall. (red)
Skriv sedan kod som uppfyller testfallet. (green)
Städa i koden, så du känner dig nöjd med din kod hittills. Fortsätt sedan med nästa AK.
  
  
AK och Krav:
1. funktionen skall returnera filtrerad lista som matchar elementen 
2. funktionen skall returnera filtrerad lista som kan matcha del av element som finns i listan
3. input skall vara av typen sträng annars skall funktionen kasta ett ett  TypeError exception
4. master_list skall vara en lista av strängar annars skall funktionen kasta ett ett  TypeError exception
5. funktionen skall inte ta hänsyn till versaler eller gemener på input
6. för att starta sökfunktionen krävs att input strängen inte är tom, om tom sträng returneras None
  
```log
.....                                                                    [100%]
5 passed in 0.02s
Finished running tests!
```
  
# Uppgift 4 - Multiplikationstabellen
Vi behöver en funktion som kan ge oss multiplikationstabellen.
Parametern "n" talar om vilket tals tabell vi ska skapa.
Parametern "limit" talar om var vi ska sluta.
Om vi till exempel frågar efter 3:ans tabell, med limit \== 4, ska programmet räkna ut:
3x1 = 3
3x2 = 6
3x3 = 9
3x4 = 12
  
```python
multiplication_table(3, 4) → [3, 6, 9, 12]
  
def muliplication_table(n, limit):
    return None  # TODO
```
  
Formulera krav och acceptanskriterier.
Kör sedan red-green-refactor för varje acceptanskriterium.
  
  
AK och Krav:
1. Funktionen tar in parameter n som talar om vilken multiplikations tabell som skall användas
2. Funktionen tar in parameter limit som talar om vilken produkt som man skall stanna på.
3. Parameter limit värde skall vara större än > 0 annars skall funktionen returnera None
4. In parametrarna skall vara av typen integer
5. Funktionen skall returnera en lista med multiplikationstabellen och med längden limit
6. Multiplikationstabellen startar med produkten 1
7. Funktionen skall returnera typen list
  
  
Notera: Boolean är en subklass av integer så går inte att testa att parametrarna är av typen boolean.
  
```log
.......                                                                  [100%]
7 passed in 0.02s
Finished running tests!
```
  
# Uppgift 5 - Balansera listor
  
Som en del i ett större program har vi en lista som kan innehålla flera element. Men elementen kan flyttas mellan denna och en annan lista. Vi behöver ett sätt att balansera listorna, så att de har lika många element - åtminstone så nära som möjligt. Ordningen på elementen är inte viktig.
  
Formulera krav och acceptanskriterier.
  
Kör sedan red-green-refactor för varje acceptanskriterium.
  
AK och Krav:
1. Funktionen tar in två listor om inte parametrarna är listor kastar man ett TypeError
2. Funktionen returnerar två listor
3. Funktionen jämför längden på listorna och skall föra över de sista elementen i listan på den längsta listan så att de blir lika långa.
4. Om antalet element på listorna inte går att få lika långa. Ex längd på lista 1 = 2 och längd på lista 2 = 5. Så skall den längsta listan få behålla ett extra element. Dvs. längderna blir då lista 1 = 3 ocjh längd på lista 2 = 4
5. Summan av antal element i listorna skall vara lika med summan av antal element av de returnerade listorna.
  
```log
.......                                                                  [100%]
7 passed in 0.02s
Finished running tests!
```

