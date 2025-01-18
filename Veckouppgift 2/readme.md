# Uppgift1
### Diskutera i grupp

Ni kan göra den här uppgiften antingen direkt, eller senare i veckan. Om ni gör den senare, passa på att kombinera med code review.

  
1. Vad är syftet med koden?  
2. Testkör koden med några olika värden.
3. Finns det några direkta fel i koden? (fel som gör att programmet kraschar)
4. Finns det logiska fel? (programmet gör något annat än det är tänkt)    
5. Diskutera möjliga lösningar på felen ni hittat.
6. Diskutera möjliga förbättringar på koden.


![[Pasted image 20250117175434.png]]

## Egna tankar:

### Vad syftet är med koden
Syftet med koden ser ut att vara någon form av bonusprogram som skall avgöra vilken rabatt som du har rätt till (dvs vilken bonusnivå man når upp till.)

### Test kör koden
Testar att fylla i att man inte skall köpa något. Då blir det traceback eftersom tom sträng inte är en float

Testar värdet 500....
```log
Välkommen, köp något dyrt: 500
Grattis! Du har avancerat till nivå 1 och får 10% rabbatt.
Grattis! Du har avancerat till nivå 2 och får 25% rabatt.
Traceback (most recent call last):
  File "c:\Users\dawa01\Documents\Python Scripts\nbi\TAPHT24D_PP\Veckouppgift 2\uppgift1.py", line 17, in <module>
    print("Efter rabatter blir priset.... " + final_price)
TypeError: can only concatenate str (not "float") to str
```

Blir traceback eftersom man inte omvandlar float till string innan man sätter in i print funktionen .


### Finns det några direkta fel i koden (fel som gör att programmet kraschar)
Ja det gör det man måste omvandla flytvärdet till en sträng.

### Finns det logiska fel? (programmet gör något annat än det är tänkt)  
Ja man får rabatt även om man att man inte är medlem. Det är nog tänkt att man skall ha en check på att man är medlem innan man räknar ut rabatten.
Rabatten behövs ju inte beräknas för icke medlemmar.

Om  man fyller i ex bokstäver eller tom sträng kraschar programmet.

Oklart vad man skall göra som användare.

Man får för mycket rabatt eftersom man har 2st oberoende if satser. vilket gör att de körs efter varandra istället för separat.
```log
Välkommen, köp något dyrt: 1000
Grattis! Du har avancerat till nivå 1 och får 10% rabbatt.
Grattis! Du har avancerat till nivå 2 och får 25% rabatt.
Efter rabatter blir priset.... 650.0
```
650-1000/1000 = 0,35 =>35% och man kunde man få 25%


### Diskutera möjliga lösningar
- Typomvandla float ---> str
- Använd en if sats för att kontrollorera att man är medlem
- Använd elif istället för två ifsatser så slipper man att rabatten får 2ggr. Kasta sedan om så att den första if satsen kommer att vara det som kollar det största värdet. Sedan elif satsen skall kolla underliggande nivåer... annars kommer man nivå1 bara att väljas. 

### Diskutera förbättringar i koden
- Fråga användaren om man vill bli medlem



# Uppgift 2

 Skriv in följande värden för att testa att ditt program gjort rätt:
121 cm (får inte åka)
130 cm (får åka)
155 cm (får åka)

### Diskutera:
#### Varför just tre värden?
- Dessa tre värden tar på samt över o under gränsen så man ser att algoritmen fungerar.
- Man täcker då int de flesta fall utan att överdriva data mängden.
#### Varför dessa värden?
- samma som punkten ovan, man ser till att vara under och över gränsen samt kontrollera vad som händer om man är precis på gränsen.

#### Skulle det vara bra att lägga till testvärdet 129 cm?
Borde inte spela så stor roll eftersom det egentligen är samma test som 121cm.


# Uppgift3

Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) 
behöver du minst tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.

spelar inte så stor roll vilka värden man kör med men kanske kan tänka att man kör med normala fotbolvärdeb.
0-10.

Har även tänkt att användaren fyllt i negativa värden... så anpassade programmet till det.


