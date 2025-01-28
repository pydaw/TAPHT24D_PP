import random

__version__ = 3

# Talserie
if __version__ == 1:
    def check_over_21():
        sum = 0
        for number in range(1,22):
            sum += number
            if sum > 21:
                print(f"Talet är '{number}' när summan är '{sum}' > 21")
                return sum
    
    
    result = check_over_21()
    print(f"Första talet i serien som är över 21 är: {result}")



# Slumpa fram kort
elif __version__ == 2:
    def check_over_21():
        sum = 0
        for i in range(1,22):
            card = random.randint(1, 13)
            sum += card
            print(f"Slumpmässigt kort: {card}")
            if sum > 21:
                print(f"Kort '{card}' när summan är '{sum}' > 21")
                return sum


    result = check_over_21()
    print(f"Summand av korten är över 21 är: {result}")


# Fråga spelare om nytt kort eller vill stanna
elif __version__ == 3:
    def check_over_21(sum):
        card = random.randint(1, 13)
        sum += card
        print(f"Slumpmässigt kort: {card}")
        if sum > 21:
            print(f"Kort '{card}', summa är'{sum}' > 21")
        return sum


    player1_sum = 0
    player1_in_game = True
    player2_sum = 0
    player2_in_game = True

    i = 0
    while (player1_in_game or player2_in_game) and (player1_sum <= 21 or player2_sum <= 21):
        i += 1
        print(f"===== Kort omgång: {i} =====")
        # Spelare 1: Riktig användare
        if player1_in_game:
            print("--- Spelare1 ---")
            while True:
                print(f"Dim summa är: {player1_sum}")
                answer = input("Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: ")
                if answer.casefold() == "ja":
                    player1_sum = check_over_21(player1_sum)
                    break       
                elif answer.casefold() == "nej":
                    print(f"Spelare 1 har stoppat på summan: {player1_sum}")
                    player1_in_game = False
                    break
                else:
                    print("Svara 'Ja' eller 'Nej'")
            print("")

        # Spelare 2: Simulerad användare
        if player2_in_game:
            print("--- Spelare2 (Dator) ---")
            while True:
                # Spelare 2 beslutar om att fortsätta eller att stanna
                print(f"Dim summa är: {player2_sum}")
                if player2_sum <= 13:
                    print("Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Ja")
                    answer = "ja"
                else:
                    print("Nytt kort eller stanna? Vill du dra ett nytt kort [Ja/Nej]: Nej")
                    answer = "nej"
                
                if answer.casefold() == "ja":
                    player2_sum = check_over_21(player2_sum)
                    break       
                elif answer.casefold() == "nej":
                    print(f"Spelare 2 har stoppat på summan: {player2_sum}")
                    player2_in_game = False
                    break
                else:
                    print("Svara 'Ja' eller 'Nej'")
            print("")
    
    if player1_sum > player2_sum and player1_sum <= 21:
        print("Spelare 1 har vunnit!")
    elif player2_sum > player1_sum and player2_sum <= 21:
        print("Spelare 2 har vunnit!")
    elif player1_sum > 21 and player2_sum > 21:
        print("Ingen har vunnit båda är över 21!")
    elif player1_sum == player2_sum:
        print("Ingen har vunnit oavgjort!")
    elif player1_sum <= 21 and player2_sum > 21:
        print("Spelare 1 har vunnit!")
    elif player2_sum <= 21 and player1_sum > 21:
        print("Spelare 2 har vunnit!")
    else:
        print(f"Summa spleare1: {player1_sum}, Summa spelare2: {player2_sum}")
    