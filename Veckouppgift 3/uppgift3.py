
__version__ = 4


if __version__ == 1:
    # Gör ett program som upprepade gånger ber användaren skriva in ett tal. 
    # När man skriver in strängen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen. Exempel:
    # Välkommen till Kvittokompis! Avsluta genom att skriva: quit
    # Skriv in ett belopp: 25
    # Skriv in ett belopp: 50
    # Skriv in ett belopp: quit
    # Det blir 75 kr totalt. Välkommen åter!

    # Tips! För att lösa uppgiften behöver du: flera variabler, input, while-loop.
    
    print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")
    sum = 0
    while True:
        user_input = input("Skriv in ett belopp: ")
        if user_input == "quit":
            print(f"Det blir {sum} kr totalt. Välkommen åter!")
            break
        else:
            sum += float(user_input)


elif __version__ == 2:
    # Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
    # Hur många är ni? 3
    # Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!
    
    print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")
    sum = 0
    while True:
        user_input = input("Skriv in ett belopp: ")
        if user_input == "quit":
            no_of_payers = int(input("Hur många är ni? "))
            print(f"Det blir {sum} kr totalt, alltså {sum/no_of_payers} kr per person. Välkommen åter!")
            break
        else:
            sum += float(user_input)



elif __version__ == 3:
    # Version 3: programmet ska fråga hur många procent dricks man vill lägga på. 
    # Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.

    print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")
    sum = 0
    while True:
        new_expense = input("Skriv in ett belopp: ")
        if new_expense == "quit":
            no_of_payers = int(input("Hur många är ni? "))
            
            tip = input("Hur många procent i dricks? (tomt = 10%) ")
            if tip == "":
                tip_percent = 10.0
            else:
                tip_percent = float(tip)

            tip_cost = sum * tip_percent / 100.0
            price_with_tip = sum + tip_cost

            print(f"Det blir {price_with_tip} kr totalt (varav {tip_cost} kr är dicks), alltså {price_with_tip/no_of_payers} kr per person (varav {tip_cost/no_of_payers} kr är dricks). Välkommen åter!")
            break
        else:
            sum += float(new_expense)


elif __version__ == 4:
    # Nice to have: prova att använda try+except eller isdigit för att hantera de fall när användaren skriver ett felaktigt värde. 
    # Python Try Except , isdigit | StackOverflow 
    # ("Nice to have" handlar om funktionalitet som inte är nödvändig, men som är bra att ha. 
    # Gå gärna vidare till nästa uppgift och återvänd till den här om du vill lära dig mer.)
    
    print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")
    sum = 0
    while True:
        new_expense = input("Skriv in ett belopp: ")

        if new_expense.isdigit() or new_expense == "quit":   
            if new_expense == "quit":
                no_of_payers = 0
                while no_of_payers < 1:    
                    try:
                        no_of_payers = int(input("Hur många är ni? "))
                        if no_of_payers < 0:
                            print("Måste ange ett positivt heltal")
                    except ValueError:
                       print("Antal personer skall skrivas in som ett heltal")
                       continue


                tip_percent = -1
                while tip_percent < 0:
                    tip = input("Hur många procent i dricks? (tomt = 10%) ")
                    if tip == "":
                        tip_percent = 10.0
                    else:
                        try:
                            tip_percent = float(tip)
                        except ValueError:
                            print("Dicks skall skrivas in som ett decimal tal (>=0%)")
                            continue
                    
                tip_cost = sum * tip_percent / 100.0
                price_with_tip = sum + tip_cost

                print(f"Det blir {price_with_tip} kr totalt (varav {tip_cost} kr är dicks), alltså {price_with_tip/no_of_payers} kr per person (varav {tip_cost/no_of_payers} kr är dricks). Välkommen åter!")
                break
            else:
                sum += float(new_expense)
        else:
            print("Felaktig värde! Ange ett tal eller avsluta med 'quit'")
            continue