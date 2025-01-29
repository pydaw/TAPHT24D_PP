from random import choice

# --- Uppgift - Pokerhand ---
# 1 Bygg en funktion som slumpar ett spelkort. 
# Den ska returnera en lista med två element: färg och valör. 
# Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess, 
# för enkelhets skull använder vi talen 2 till 14.
# Exempel på ett kort: ["hjärter", 12]


# 2 Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.


# 3 Bygg första versionen av poker_hand(cards). 
# Med hjälp av de andra funktionerna ska den ta reda på om man har ett par, 
# dvs det finns två kort med samma valör.


# Fortsätt att lägga till fler kontroller till funktionen.
# Tips! Du kan göra en funktion som skriver ut kortvärdet snyggare:
# pretty_print_card(["hjärter", 5]) → "hjärter fem"

# Lista med pokerhänder.
# Ett par (två lika kort)
# Två par
# Tretal (tre lika)
# Straight (5 kort i följd, t.ex. 7-8-9-10-11)
# Flush / färg (alla kort har samma färg)
# Hus (par och tretal med olika valörer)
# Fyrtal
# Straight flush (5 kort i följd, med samma färg)
# Femtal
# ----------------------------


def get_random_card():
    """ 
    (1) Funktion som slumpar ett spelkort
    """
    colors = [ "hjärter", "spader", "ruter", "klöver"]
    value = [i for i in range(2,14+1)]
    return [choice(colors), choice(value)]


def is_card_value_equal(card1, card2):
    """
    (2) Funktion som jämför två spelkort och kan tala om ifall de har samma valör
    """
    return card1[1] == card2[1]


def get_five_random_cards():
    """
    Funktion som returnerar fem slumpvisa kort

    Return: Lista med fem slumpvisa kort Ex. [['hjärter', 6], ['hjärter', 13], ['klöver', 6], ['hjärter', 5], ['spader', 8]]
    """
    # Ta fram fem kort
    cards = []
    while len(cards) < 5:
        
        # Ta ett nytt kort
        new_card = get_random_card()
        
        if len(cards) > 0:

            # Kontrollera om exakt samma kort redan finns (skall ej vara möjligt)
            same_card = False
            for card in cards:
                if card == new_card:
                    same_card = True
            
            # Om samma kort ta ett nytt kort, kör while loopen en gång till
            if same_card:
                continue

        # Lägg till nytt kort i listan
        cards.append(new_card)

    return cards


def get_cards_with_equal_values(cards):
    """
    Funktion som tar en lista med kort och returnerar hur många gånger värdet förekommer

    Parameter:  cards    -   Lista på kort Ex. [['hjärter', 6], ['hjärter', 13], ['klöver', 6], ['hjärter', 5], ['spader', 8]]
    Return: Returnerar en lista hur många ggr ett kortvärde förekommer. Ex. [[6,3], [4,2]] = Värdet 6 förkommer 3 ggr och värdet 4 förekommer 2ggr
    """
    
    # Kontrollera om det finns kort som har samma valör
    equal_cards = []
    for card1 in cards:
        for card2 in cards:

            # Hoppa över om samma kort jämförs används
            if cards.index(card1) == cards.index(card2):
                continue
            
            # Par hittat samt kontrollera att det inte är samma kort som hittas innan (dvs omvänd ordning på jämförelsen)
            if is_card_value_equal(card1, card2) and (card1 not in equal_cards or card2 not in equal_cards):
                if card1 not in equal_cards: 
                    equal_cards.append(card1)
                if card2 not in equal_cards: 
                    equal_cards.append(card2)
            
    # Skapa en lista med bara värden på korten
    equal_values = [item[1] for item in equal_cards]

    # Tar bort dubletter i listan med kort värden
    equal_values = list(dict.fromkeys(equal_values))

    # Kontrollera hur många kort av varje valör det finns
    same_values = []
    for value in equal_values:
        
        # Nollställ räknare vid varje nytt värde
        count = 0
        
        # Loopa igenom varje kort
        for card in equal_cards:
            card_value = card[1]
            
            # Om man hittar ett kort med samma valör räknar man upp 'counter' med 1
            if card_value == value:
                count += 1

        same_values.append([value, count])
    return same_values


def is_all_cards_equal_in_color(cards):
    """
    Funktion som tar en lista med kort och returnerar om alla kort har samma färg.

    Parameter:  cards    -   Lista på kort Ex. [['hjärter', 6], ['hjärter', 13], ['klöver', 6], ['hjärter', 5], ['spader', 8]]
    Return: Returnerar True om alla kort är i samma färg annars returneras False
    """

    # Skapa en lista med bara färger på korten
    card_colors = [card[0] for card in cards]
    
    # Skapa en lista med första kortets färg med samma längd som antal kort
    card1_color = list(cards[0])[0]
    card1_color_compare_list = [card1_color] * len(cards)

    # Jämför om listorna är samma, dvs. har samma färg som första kortet
    return card_colors == card1_color_compare_list


def is_all_cards_in_value_order(cards):
    """
    Funktion som tar en lista med kort och returnerar om alla kort är i följd Ex. 7-8-9-10-11.

    Parameter:  cards    -   Lista på kort Ex. [['hjärter', 6], ['hjärter', 13], ['klöver', 6], ['hjärter', 5], ['spader', 8]]
    Return: Returnerar True om alla kort är i föld (Ex. 7-8-9-10-11), annars returneras False
    """
    
    # Skapa en lista med bara värden på korten
    card_values = [card[1] for card in cards]

    # Sortera listan
    card_values = sorted(card_values)

    # Gör en jämförelse lista i numerföljd från värdet av första kortet i den sorterade listan, listan är i samma längd som antal kort
    compare_values = [card_values[0]+i for i in range(len(cards))]

    return card_values == compare_values

def pretty_print_card(card):
    card_color = card[0]
    card_value = card[1]

    value_to_text = {
        2 : "två",
        3 : "tre",
        4 : "fyra",
        5 : "fem",
        6 : "sex",
        7 : "sju",
        8 : "åtta",
        9 : "nio",
        10 : "tio",
        11 : "knekt",
        12 : "dam",
        13 : "kung",
        14 : "ess",
    }
    return f"{card_color} {value_to_text[card_value]}"


if __name__ == "__main__":
    
    cards = get_five_random_cards()
    cards = [['hjärter', 14], ['hjärter', 11], ['hjärter', 3], ['hjärter', 12], ['hjärter', 10]]
    
    poker_hand_pretty_printed = ", ".join(pretty_print_card(card) for card in cards)
    print(f"Aktuell pokerhand: {poker_hand_pretty_printed}")

    # Tar fram en lista med hur många gånger ett visst värde förekommer 
    # Ex. [[6,3], [4,2]] = Tretal i sexor och Par i fyror
    card_values_occurrence = get_cards_with_equal_values(cards)

    # Kontrollera om korten är i följd
    all_card_is_in_value_order = is_all_cards_in_value_order(cards)
    
    # Kontrollera om korten är i samma färg
    all_cards_have_same_color = is_all_cards_equal_in_color(cards)



    # ### Ta fram resultatet av pokerhanden ###

    # Lista med pokerhänder:
    # [x] Ett par (två lika kort)
    # [x] Två par
    # [x] Tretal (tre lika)
    # [x] Straight (5 kort i följd, t.ex. 7-8-9-10-11)
    # [x] Flush / färg (alla kort har samma färg)
    # [x] Hus (par och tretal med olika valörer)
    # [x] Fyrtal
    # [x] Straight flush (5 kort i följd, med samma färg)
    # [x] Femtal <--- ommöjligt att få, tillagd pga kravspec.

    # Kontrollerar om man har lika kort dvs. par - femtal (fyrtal i praktiken) samt två par och hus
    count_pair = 0
    count_three_of_a_kind = 0
    for element in card_values_occurrence:
        value, no_of_occurrence = element

        value_to_text = {
            2 : "två",
            3 : "tre",
            4 : "fyra",
            5 : "fem",
            6 : "sex",
            7 : "sju",
            8 : "åtta",
            9 : "nio",
            10 : "tio",
            11 : "knekt",
            12 : "dam",
            13 : "kung",
            14 : "ess"
        }
        
        # Ett par (två lika kort)
        if no_of_occurrence == 2:
            print(f"Du fick 'Par' med valören '{value_to_text[value]}'")
            count_pair += 1
        
        # Tretal (tre lika)
        elif no_of_occurrence == 3:
            print(f"Du fick 'Tretal' med valören '{value_to_text[value]}'")
            count_three_of_a_kind += 1
         
        # Fyrtal
        elif no_of_occurrence == 4:
            print(f"Du fick 'Fyrtal' med valören '{value_to_text[value]}'")
        
        # Femtal
        elif no_of_occurrence == 5:   # <---- Omöjligt då det bara finns fyra färger
            print(f"Du fick 'Femtal' med valören '{value_to_text[value]}'")
        
        # Två par
        if count_pair == 2:
            print("Du fick 'Två par'")

        # Hus
        if count_pair == 1 and count_three_of_a_kind == 1:
            print("Du fick 'Hus'")

    # Kontrollera om mman har straight, flush, straight flush eller att det inte fanns någon pokerhand alls
    if all_cards_have_same_color and  all_card_is_in_value_order:
        print("Du fick 'Straight Flush'")
    elif all_card_is_in_value_order:
        print("Du fick 'Straight'")
    elif all_cards_have_same_color:
        print("Du fick 'Flush'")
    elif not (all_cards_have_same_color or  all_cards_have_same_color) and len(card_values_occurrence) == 0:
        print("Du fick inte så bra pokerhand!")