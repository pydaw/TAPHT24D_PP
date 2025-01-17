# is_member= False
# level1 = 100
# level2 = 300
# discount = 0

# price = input("Välkommen, köp något dyrt: ")
# price = float(price)

# if price > level1:
#     print("Grattis! Du har avancerat till nivå 1 och får 10% rabbatt.")
#     discount = discount + 10
# if price >= level2:
#     print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
#     discount = discount + 25

# final_price = price * (100 - discount) / 100
# print("Efter rabatter blir priset.... " + final_price)



# Justering av koden
# is_member= False
is_member= True
level1 = 100
level2 = 300
discount = 0

price = input("Välkommen, köp något dyrt: ")
price = float(price)

if is_member:
    if price >= level2:
        print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
        discount = discount + 25
    elif price > level1:
        print("Grattis! Du har avancerat till nivå 1 och får 10% rabbatt.")
        discount = discount + 10

final_price = price * (100 - discount) / 100
print("Efter rabatter blir priset.... " + str(final_price))