# Sportresultat
# Tottenham spelar mot Liverpool i Champions League. 
# Skriv ett program som frågar användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.

# Exempel på output:

# Matchen är över, nu ska vi räkna ut resultatet!
# Hur många mål gjorde Tottenham? 2
# Hur många mål gjorde Liverpool? 1
# Tottenham vann!


print("Matchen är över, nu ska vi räkna ut resultatet!")
goals_to_tottenham = int(input("Hur många mål gjorde Tottenham? "))
goals_to_liverpool = int(input("Hur många mål gjorde Liverpool? "))

negative_inputs = goals_to_liverpool < 0 or goals_to_tottenham < 0
if goals_to_liverpool > goals_to_tottenham and not negative_inputs:
    print("Liverpool vann!")
elif goals_to_liverpool < goals_to_tottenham and not negative_inputs:
    print("Tottenham vann!")
    

# Version 2: programmet ska tala om ifall det blev oavgjort.
elif goals_to_liverpool == goals_to_tottenham and not negative_inputs:
    print("Oavgjort!")

# Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
# Tottenham vann med 1 mål!

# Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) 
# behöver du minst tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.

else:
    print("Okänt fel")


won_with_goals = abs(goals_to_tottenham - goals_to_liverpool)
if won_with_goals > 0 and not negative_inputs:
    print(f"Vann med {won_with_goals} mål!")