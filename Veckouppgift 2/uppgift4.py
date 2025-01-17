__author__ = "Daniel Wärnelöv"
__version__ = "3.0.0"


# Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
# Version 1, exempel på output:

# Skriv in en temperatur i grader Celsius: 22
# Det blir 71.6 grader Fahrenheit.

# Version 2: fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit. Sedan räknar programmet om till den andra temperaturen.
# Tips: be användaren skriva in t.ex. "F" om man vill ange temperaturen i i Fahrenheit. 
# Använd sedan if + else.

# Version 3: om temperaturen som omvandlas är under 10°C ska programmet dessutom säga till användaren att ta på sig vinterkläder. 
# Och om temperaturen är minst 20°C ska det föreslå att man packar badkläder.

# Formel för konvertering mellan temperaturenheter:
# C = (F - 32) / 1.8
# F = 1.8 * C + 32

# Förslag på värden att testa med:

# ° Celsius |   ° Fahrenheit
# ----------------------------
# 0         |   32
# -17.777…  |   0
# 37.777…   |   100
# 100       |   212

print(f"Temperaturomvandling v{__version__}")
    
if __version__ == "1.0.0":
    print("Celcius --> Fahrenheit")
    C = float(input("Skriv in temperatur [°C]: "))
    F = 1.8 * C + 32

    print(f"Det blir {F}°F.")



elif __version__ == "2.0.0":
    user_choice = input("Vilken enhet skall temperaturen omvandlas till [C/F]: ")
    
    # Check choice with both with lower and upper case
    convert_to_fahrenheit = user_choice == "F" or user_choice == "f"
    convert_to_celcius = user_choice == "C" or user_choice == "c"

    if convert_to_fahrenheit:      
        print("Celcius --> Fahrenheit")
        C = float(input("Skriv in temperatur [°C]: "))
        F = 1.8 * C + 32

        print(f"Det blir {F}°F.")
    
    elif convert_to_celcius:
        print("Fahrenheit --> Celcius")
        F = float(input("Skriv in temperatur [°F]: "))
        C = (F - 32) / 1.8

        print(f"Det blir {C}°C.")
    
    else:
        print("Val av konverteringsenhet misslyckades!")
      


elif __version__ == "3.0.0":
    user_choice = input("Vilken enhet skall temperaturen omvandlas till [C/F]: ")
    
    # Check choice with both with lower and upper case
    convert_to_fahrenheit = user_choice == "F" or user_choice == "f"
    convert_to_celcius = user_choice == "C" or user_choice == "c"

    # Init parameter (will be overwritten during conversion)
    C = 0
    F = 0

    if convert_to_fahrenheit:      
        print("Celcius --> Fahrenheit")
        C = float(input("Skriv in temperatur [°C]: "))
        F = 1.8 * C + 32

        print(f"Det blir {F}°F.")
    
    elif convert_to_celcius:
        print("Fahrenheit --> Celcius")
        F = float(input("Skriv in temperatur [°F]: "))
        C = (F - 32) / 1.8

        print(f"Det blir {C}°C.")
    
    else:
        print("Val av konverteringsenhet misslyckades!")
        exit() # End script

    # Message to user when cold or hot...
    if C < 10.0:
        print("Det är kallt, ta på dig vinterkläder!")
    elif C >= 20:
        print("Det varmt, packa badkläder!")