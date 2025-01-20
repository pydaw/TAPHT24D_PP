# Gör ett spel som slumpar ett hemligt tal mellan 1 och 100. Sedan ska man försöka gissa det. 
# Om man gissar för lågt eller för högt ska spelet tala om det. Efter att man har gissat rätt ska spelet skriva ut antalet gissningar.

# Slumpa ett hemligt tal
# secret = random.randint(1, 100)

# Exempel:
# Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?
# Gissa: 40
# Nej, det är för lågt!
# Gissa: 55
# Nej, det är för högt!
# Gissa: 51
# Det är rätt!! Du gjorde det på 3 gissningar.

# Version 2: skriv ut om man är nära ifall man gissar högst 5 ifrån det rätta svaret.
# "Nu börjar det brännas!"



import random

__version__ = 2


# Version 1
if __version__ == 1:

    secret = random.randint(1,100)

    print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")

    no_of_guesses = 0
    while True:
        guess = int(input("Gissa: "))
        no_of_guesses += 1

        if guess == secret:
            print(f"Det är rätt!! Du gjorde det på {no_of_guesses} gissningar.")
            break
        elif guess > secret:
            print("Nej, det är för högt!")
        elif guess < secret:
            print("Nej, det är för lågt!")
        

# Version 2
elif __version__ == 2:

    secret = random.randint(1,100)

    print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")

    no_of_guesses = 0
    while True:
        guess = int(input("Gissa: "))
        no_of_guesses += 1
        
        near = ""
        if abs(guess - secret) <= 5:
            near = "Nu börjar det brännas!\n"

        if guess == secret:
            print(f"Det är rätt!! Du gjorde det på {no_of_guesses} gissningar.")
            break
        elif guess > secret:
            print(f"{near}Nej, det är för högt!\n")
        elif guess < secret:
            print(f"{near}Nej, det är för lågt!\n")
        
