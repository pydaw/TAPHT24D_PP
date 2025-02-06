import module
from pytest import approx


# 1
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
    

# 2
def test_count_words():
    assert module.count_words("Hej hopp i lingonskogen!") == 4
    assert module.count_words("Hej        hopp i lingonskogen!") == 4
    assert module.count_words("Hej!") == 1
    assert module.count_words("") == 0
    assert module.count_words(["Hej","på","dej!"]) is None
    assert module.count_words(True) is None
    assert module.count_words(32) is None
    

# 3
def test_find_median():
    assert module.find_median([1,2,1000]) == 2
    assert module.find_median([1,100,1000,100]) == 100
    assert module.find_median([1.0,2.0,1000.0]) == 2.0
    assert module.find_median([1]) == 1
    assert module.find_median([]) is None
    assert module.find_median([1,True,"str"]) is None
    assert module.find_median("1234") is None
    assert module.find_median(1234) is None
    assert module.find_median(True) is None