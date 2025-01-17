
# Gammal kod:
# x = 100  # biljettpris
# y = 200  # pengar på fickan
# print("Det blir " + (y - x) " kronor över.")
# z = 200 - 100 / 2
# print("Hälften är: " + z)


# Ändrad kod:
# - Skiver bättre variabelnamn så man vet vad variabeln gör, kan då ta bort kommentar.
# - Rättat matte, delade inte hela värdet med 2
# - lagt till extra variabler för att lättare kunna följa koden samt att uträkning ligger bara på ett ställe istället för två
# - gjort typomvanlding med str() så att nummret kan skrivas ut.


ticket_price = 100
money_available = 200
money_after_purchase = money_available - ticket_price
print("Det blir " + str(money_after_purchase) + " kronor över.")

half_of_money_after_purchase = money_after_purchase / 2
print("Hälften är: " + str(half_of_money_after_purchase))
