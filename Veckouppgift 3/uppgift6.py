# Todo list (att göra-lista)
# Bygg ett program där användaren kan lägga till saker till en todo-lista.
# Tips: använd en loop, input och en variabel för listan.
# Exempel:

# ** Todo list extravaganza **
# 1. Se innehållet i din lista
# 2. Lägga till nya punkter i din lista
# Välj ett alternativ: 1
# Din lista är tom
# .
# Välj ett alternativ: 2
# Skriv in en ny sak du måste komma ihåg att göra: mata guldfisken
# Ok, lade till "mata guldfisken" i listan.
# .
# Välj ett alternativ: 1
# + Mata guldfisken
# .

# Version 2: lägg till ett menyalternativ, "Markera som klar". 
# När användaren väljer det, ska programmet fråga efter vilken grej man är färdig med. Den färdiga grejen ska tas bort från listan.

# Version 3: lägg över färdiga grejer i en ny lista. 
# Användaren ska kunna välja vad man har bockat av tidigare, eller välja att lägga tillbaka grejen i todo-listan.


__version__ = 3


# Version 1
if __version__ == 1:

    print("** Todo list extravaganza **")

    todo_list = []
    while True:
        print("1. Se innehållet i din lista")
        print("2. Lägga till nya punkter i din lista")
        print("quit. Avsluta")
        
        choice = input("Välj ett alternativ: ")
        
        # Avsluta programmet
        if choice == 'quit':
            print("Avslutar programmet")
            break

        # Titta i listan
        elif choice == "1":
            if len(todo_list) > 0:
                for element in todo_list:
                    print(f"+ {element}")
            else:
                print("Din lista är tom")
            print(".")
        
        # Lägga till i listan
        elif choice == "2":
            new_task = input("Skriv in en ny sak du måste komma ihåg att göra: ")
            todo_list.append(new_task)
            print(f'Ok, lade till "{new_task}" i listan')
            print(".")


# Version 2
elif __version__ == 2:
    print("** Todo list extravaganza **")

    todo_list = []
    while True:
        print("1. Se innehållet i din lista")
        print("2. Lägga till nya punkter i din lista")
        print("3. Markera som klar")
        print("quit. Avsluta")
        
        choice = input("Välj ett alternativ: ")
        
        # Avsluta programmet
        if choice == 'quit':
            print("Avslutar programmet")
            break
        
        # Titta i listan
        elif choice == "1":
            if len(todo_list) > 0:
                for element in todo_list:
                    print(f"+ {element}")
            else:
                print("Din lista är tom")
            print(".")
        
        # Lägga till i listan
        elif choice == "2":
            new_task = input("Skriv in en ny sak du måste komma ihåg att göra: ")
            todo_list.append(new_task)
            print(f'Ok, lade till "{new_task}" i listan')
            print(".")
        
        # Klarmarkera
        elif choice == "3":
            ready_task = input("Ange vilken uppgift som skall klarmarkeras?: ")
            try:
                todo_list.remove(ready_task)
                print(f'Ok, tagit bort "{ready_task}" från listan')
            except ValueError:
                print(f'Kan inte hitta "{ready_task}" i listan')
            print(".")


# Version 3
elif __version__ == 3:
    print("** Todo list extravaganza **")

    todo_list = []
    done_list = []
    while True:
        print("1. Se innehållet i din lista")
        print("2. Lägga till nya punkter i din lista")
        print("3. Markera som klar")
        print("quit. Avsluta")
        
        choice = input("Välj ett alternativ: ")
        
        # Avsluta programmet
        if choice == 'quit':
            print("Avslutar programmet")
            break
        
        # Titta i listan
        elif choice == "1":
            if len(todo_list) > 0:
                for element in todo_list:
                    print(f"+ {element}")
            else:
                print("Din lista är tom")
            print(".")
        
        # Lägga till i listan
        elif choice == "2":
            if len(done_list) > 0:
                i = 0
                print("Klarmarkerade uppgifter:")
                for element in done_list:
                    print(f"{i}: {element}")
                    i += 1
                print("")
            new_task = input("Skriv in en ny sak du måste komma ihåg att göra (använd nummer för att välja gammal uppgift): ")
            try:
                if new_task.isdigit():
                    new_task = done_list.pop(int(new_task))
                todo_list.append(new_task)
                if new_task in done_list:
                    done_list.remove(new_task)
                print(f'Ok, lade till "{new_task}" i listan')
            except ValueError:
                print(f'Kan inte tabort "{new_task}" ur klarlistan')    
            print(".")
        
        # Klarmarkera
        elif choice == "3":
            if len(done_list) > 0:
                i = 0
                print("Klarmarkerade uppgifter:")
                for element in done_list:
                    print(f"{i}: {element}")
                    i += 1
                print("")
            ready_task = input("Ange vilken uppgift som skall klarmarkeras?: ")
            try:
                todo_list.remove(ready_task)
                done_list.append(ready_task)
                print(f'Ok, tagit bort "{ready_task}" från listan')
            except ValueError:
                print(f'Kan inte hitta "{ready_task}" i listan')
            print(".")