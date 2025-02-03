# Uppgift1:
# Skriv ner vad du tror kommer skrivas ut. 
# Skriv sedan in koden i din IDE, exakt som den står, och kör den. 
# Fick du samma resultat som du trodde? Om inte, varför?



# 1 Vilka ekvivalensklasser har uttrycken?
# 1a. 
# x > 100  
# Alla talen som är strikt större än 100

# 1b. 
# y == 42 
# Tal som är lika med 42

# 1c. 
# len(text) >= 5  
# Om strängen eller listan har längden 5 eller är längre 

# 1d. 
# z == True  
# Om booleanen är True

# 1e. 
# 8 < v < 16  
# v skall vara mellan 8 och 16, dvs strikt mindre 16 och över 8

# 1f. 
# w == 32 or w == 64 or w == 128  
# Variablen w får endast anta värdena 32, 64 eller 128

# 1g. 
# if x < 5: … elif x < 10: … elif x < 15: … else  
# Det finns 4st ekvivalensklasser, dvs om:  
# 1: x är strikt mindre än 5
# 2: x är strikt mindre än 10 men strörre eller lika med 5
# 3: x är strikt mindre än 15 men strörre eller lika med 10
# 4: När x antar andra värden ex strörre eller lika med 5 eller alla andra fall ex sträng



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
    return 0

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

# Själva testerna i sig dvs assert kommandona ser bra ut
# men skulle säkert behöva delas upp i olika tester, 
# för att om något test fallerar så ser man inte hur de andra assert testerna  gick


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
