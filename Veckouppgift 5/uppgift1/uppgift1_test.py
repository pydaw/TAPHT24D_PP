# Uppgift1:
# Skriv ner vad du tror kommer skrivas ut. 
# Skriv sedan in koden i din IDE, exakt som den står, och kör den. 
# Fick du samma resultat som du trodde? Om inte, varför?



# 1 Vilka ekvivalensklasser har uttrycken?
# 1a. 
# x > 100

# Villkoret blir True om 'x': Är en int eller float som är strikt större än 1000
# Villkoret blir False om 'x': Är int eller float som är lika med 100 eller mindre. Samt om 'x' är en boolean. 


# 1b.
# y == 42

# Villkoret blir True om 'y:' Är int eller float som är lika med 42
# Villkoret blir False om 'y:' Är int eller float som inte är lika 42, samt alla andra domäner.


# 1c. 
# len(text) >= 5

# Villkoret blir True om 'text': Är en sekventiell domän som har längden 5 eller längre.
# Villkoret blir False om 'text': Är sekventiell domän som en längd som är strikt under 5.


# 1d. 
# z == True

# Villkoret blir Trure om 'z': Är boolean eller boolerskt uttryck som är lika med True.
# Villkoret blir False om 'z': Är boolean eller boolerskt uttryckt som är lika med värdet False, samt all andra domäner.


# 1e.
# 8 < v < 16

# Villkoret blir Trure om 'v':  Är int eller float som är strikt större än 8 samt strikt mindre än 16.
# Villkoret blir False om 'v:  Är int eller float som är lika med 8 eller mindre eller 16 eller större. Booleska uttryck och boolean ger också False.


# 1f. 
# w == 32 or w == 64 or w == 128

# Villkoret blir True om 'w': Är lika med int eller float som antar värdena 32, 64 eller 128.
# Vilkoret blir False om 'w': Är andra int eller float värden, eller tillhör en annan domän.


# 1g. 
# if x < 5: … elif x < 10: … elif x < 15: … else

# Villkoret för x < 5 blir True om 'x' är: Int eller float som är strikt mindre än 5, samt om variabeln är en boolean.
# Villkoret för x < 10 blir True om 'x' är: Int eller float som är lika med 5 eller större ock strikt mindre än 10.
# Villkoret för x < 15 blir True om 'x' är: Int eller float som är lika med 10 eller större och strikt mindre än 15. 
# Villkoret för att komma till else är: Int eller float som är lika med 15 eller större. 



# 2 Det har smugit sig in kommentarer i stället för kod på några ställen. 
# Skriv färdigt testfallen test_empty_list och test_number_list.

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


# 3a Diskutera följande kod. 
# Räcker det med ett testfall för att testa funktionen?

# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
def count_vowels(word):
    return None

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

# Själva testerna i sig dvs assert kommandona ser bra ut men kana delas upp i olika tester,
# för att förhindra att något test fallerar så syns inte hur de andra assert testerna gick.


# 3b Skriv färdigt funktionen count_vowels med hjälp av TDD-metoden, red → green → refactor.

# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
def count_vowels(word):
    return 0

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

# Här så returnerar vi 0 då kommer testet att gå igenom. 
# Man får sedan skriva mer tester för att skriva färdigt funktionen med rätt innehåll.


# 4 Formulera testfall för en funktion som hittar största talet i en lista.

# Returnerar det största talet i listan
# Returnerar None om det inte finns något
def find_max(list):
    None


def test_greatest_number_in_list():
    excepted = 80
    actual = find_max([60, 30, 80, 1])

    assert actual == excepted


def test_greatest_number_in_list_is_none_when_list_is_empty():
    excepted = None
    actual = find_max([])

    assert actual == excepted


# 5 Winner takes it all brukar det ju heta, men nu ska vi försöka ge lite heder åt alla andrapristagare. 
# Formulera testfall för en funktion som hittar näst största talet i en lista!

# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet
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
