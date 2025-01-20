import time
from os import system, name

# Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.

# for y in range(1, 7):
#     s = ""
#     for x in range(1, 9):
#         if x == y:
#             s += "#"
#         else:
#             s += "."
#     print(s)

# Loopar igenom figurerna a-j visas upp i 3s

# Rensa terminalfönstret
def clear():
    # för windows
    if name == 'nt':
        _ = system('cls')

    # för mac eller linux
    else:
        _ = system('clear')



if __name__ == "__main__":
    while True:
        sequence = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        for figure in sequence:
            clear()
            print(f"==== Figur: {figure} ====")
            
            if figure == "a":
                for y in range(1, 7):
                    s = ""
                    for x in range(1, 9):
                        if x == 1:
                            s += "#"
                        else:
                            s += "."
                    print(s)

            elif figure == "b":
                for y in range(1, 7):
                    s = ""
                    for x in range(1, 9):
                        if x == y:
                            s += "#"
                        else:
                            s += "."
                    print(s)

            elif figure == "c":
                for y in range(1, 7):
                    s = ""
                    for x in range(1, 9):
                        if 3 <= x <= 5:
                            s += "#"
                        else:
                            s += "."
                    print(s)

            elif figure == "d":
                for y in range(1, 7):
                    s = ""
                    for x in range(1, 9):
                        if x == 3 or y == 3:
                            s += "#"
                        else:
                            s += "."
                    print(s)

            elif figure == "e":
                for y in range(1, 7):
                    s = ""
                    for x in range(1, 9):
                        if x == 5 or x == 7-y:
                            s += "#"
                        else:
                            s += "."
                    print(s)

            elif figure == "f":
                for y in range(1, 7):
                    s = ""
                    for x in range(1, 9):
                        if x == y or x == 7-y:
                            s += "#"
                        else:
                            s += "."
                    print(s)

            elif figure == "g":
                for y in range(1, 7):
                    s = ""
                    for x in range(1, 9):
                        # Varje udda tal
                        if x % 2 == 1:
                            s += "#"
                        else:
                            s += "."
                    print(s)

            elif figure == "h":
                for y in range(1, 7):
                    s = ""
                    for x in range(1, 9):
                        if (2 <= x <= 7 and 2 <= y <= 5) and not (3 <= x <= 6 and 3 <= y <= 4 ):
                            s += "#"
                        else:
                            s += "."
                    print(s)

            elif figure == "i":
                for y in range(1, 7):
                    s = ""
                    for x in range(1, 9):
                        if x % 3 == (y + 1) % 3 :
                            s += "#"
                        elif x % 3 == (y + 2) % 3:
                            s += "O"
                        else:
                            s += "."
                    print(s)

            elif figure == "j":
                for y in range(1, 7):
                    s = ""
                    for x in range(1, 9):
                        if (x % 3 == 0 and y <= 3) or \
                        ( x % 2 == 0 and y == 5) or \
                        ( x % 2 == 1 and y == 6) :
                            s += "#"
                        else:
                            s += "."
                    print(s)
            time.sleep(3)