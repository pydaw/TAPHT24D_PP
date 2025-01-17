# 1a 
# Det är ca 470 km mellan Stockholm och Göteborg. 
# Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg. 
# Du behöver fråga användaren hur fort man ska köra, i km/h.
# Tips: omvandla till m/s genom att dela med 3,6. Sedan kan du använda formeln: tid = sträcka / hastighet.

distance = 470  # [km]
# speed = int(input("Vilken hastighet skall köras [km/h]: "))
speed = 80
calculated_time_in_h = distance/speed
print("Tid Sthlm --> Gbg: " + str(calculated_time_in_h) + "h")

# 1b 
# Gör så att programmet svarar i minuter i stället för timmar.
calculated_time_in_min = calculated_time_in_h * 60
print("Tid Sthlm --> Gbg: " + str(calculated_time_in_min) + "min")

# 1c 
# (svårare) Nu ska programmet svara i hela timmar och minuter.
# Tips: använd operatorerna // och %. Heltalsdivision // dividerar och avrundar nedåt till närmaste heltal. 
# Procent % räknar ut resten vid division med heltal. Exempel:
# 3 // 2 == 1      (3 / 2 == 1.5, avrundar nedåt)
# 60 % 60 == 0  (ingen rest)
# 70 % 60 == 10  (10 i rest)
# Be en AI förklara heltalsdivision och modulo i Python om du känner dig osäker!

hours = round(calculated_time_in_min // 60)
minutes = round(calculated_time_in_min % 60)
print("Tid Sthlm --> Gbg: " + str(hours) + ":" +  str(minutes) + " [hh:mm]")


