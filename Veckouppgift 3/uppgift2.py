# 1a,
# Skriv färdigt kodexemplet.
# answer = 0
# for i in ????????????:
#     answer += i
# print("Summan av talen 1 till 10 är: " + str(answer))
# # Svaret ska bli 55

answer = 0
for i in range(1,11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55


# 1b,
# Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)

answer = 0
for i in range(1,101):
    answer += i
print("Summan av talen 1 till 100 är: " + str(answer))
# Svaret ska bli 5050


# 1c, 
# Skriv om 1b så att den använder en while-loop.
answer = 0
i = 1
while i < 101:
    answer += i
    i += 1
print("Summan av talen 1 till 100 är: " + str(answer))
# Svaret ska bli 5050


# 2, 
# Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]

data = [1, -2, 3, -2, 4, -3]
sum = 0
for element in data:
    sum += element
print("Summan av alla element i listan: " + str(sum))


# 3 
# Träna på att skapa och manipulera listor. Alla uppgifter ska lösas med funktionerna som står i presentationen.

# 3a 
# Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan 2med funktionen print.

filmer = ["Start Wars: A New Hope", "Start Wars: The Empire Strikes Back", "Start Wars: Return Of The Jedi", "Start Wars: The Force Awakens"]
# Står egentligen att man skall printa listan i 2 med print men antar att det skall vara den listan vi precis gjort
print(filmer)


# 3b, 
# Lägg till "Fellowship of the ring" sist i listan.
filmer.append("Fellowship of the ring")
print(filmer)


# 3c,
# Lägg till "The two towers" på första platsen i listan. (index noll)
filmer.insert(0, "The two towers")
print(filmer)


# 3d 
# Ta reda på vilken position (index) "Fellowship of the ring" har nu.
index = filmer.index("Fellowship of the ring")
print("'Fellowship of the ring' ligger på index: " + str(index))


# 3e 
# Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
filmer.remove("Start Wars: The Empire Strikes Back")
index = filmer.index("Fellowship of the ring")
print("'Fellowship of the ring' ligger nu på index: " + str(index))


# 3f Ta reda på hur lång listan är. (len)
print(f"Längden på listan med filmer är {len(filmer)} element lång")


# 3g 
# Vänd listan baklänges.
filmer.reverse()
print(f"Detta är listan baklänges: {filmer}")


# 3h 
# Sortera listan stigande i bokstavsordning.
filmer.sort()
print(f"Sorterad lista: {filmer}")

