from datetime import date, timedelta

# 3a 
# Skriv ett program som talar om dagens datum.
# Resurs: Hantera datum i Python 

today = date.today()
print(f"Dagens datum: {today}")


# 3b 
# (svårare) Ändra programmet så att det kan tala om vilket datum det är om 7 dagar.
days = 7
future_date = date.today() + timedelta(days=days)
print(f"Om {days} dagar är det datum '{future_date}'")