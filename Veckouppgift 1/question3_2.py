# 2a 
# Nu är det dags att köpa vinterkläder. 
# Du ser en fin jacka som kostar 2000 kronor. 
# Jackan är på rea, 50%. Skriv ett program som räknar ut hur mycket du behöver betala.
# Tips: räkna ut rabatten med formeln: slut_pris = pris * rea_procent / 100.

price = 2000 # [kr] - Pris på jacka
discount = 50 # [%]

price_after_discount = price*(100-discount)/100
print("Summa att betala: " + str(price_after_discount))


# 2b 
# Gör om programmet så att användaren kan skriva in en procentsats.
# Testa genom att hitta på en procentsats och räkna ut vad programmet ska svara med, 
# innan du kör det. Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800 kr.


price = 2000 # [kr] - Pris på jacka
discount = int(input("Ange rabatt i procent: "))

price_after_discount = price*(100-discount)/100
print("Summa att betala: " + str(price_after_discount))