import module

# ======================================================================
# OBS! Testfallen ligger i test_main.py, för att kunna köra med pytest
# ======================================================================

# 1 - Funktion som tar antalet grader och returnerar
# Ta fram vilka domäner som kan användas till testfallet
print("==== 1 ====")
print(module.c_to_f(-500))
print(module.c_to_f(500))
print(module.c_to_f(True))
print(module.c_to_f(1))
print(module.c_to_f(False))
print(module.c_to_f(0))
# print(module.c_to_f("Sträng"))
# print(module.c_to_f(None))


# 2 - Funktion som tar in en sträng och returnerar antalet ord i stängen
print("==== 2 ====")
print(module.count_words("Hej hopp i lingonskogen!"))
print(module.count_words("Hej        hopp i lingonskogen!"))


# 3 - Funktion som tar en lista med tal och returnerar medianen
print("==== 3 ====")
print(module.find_median([1,2,1000]))
print(module.find_median([1,2,1000,100,2]))
print(module.find_median([1,2,1000,100,2,22]))
print(module.find_median([1,2]))
print(module.find_median([1]))
print(module.find_median([]))


# 4 - Funktion ska returnera `True` om listan numbers är sorterad i stigande ordning, 
# `False` annars
print("==== 4 ====")
print(module.is_sorted_ascending([1,2,1000]))

