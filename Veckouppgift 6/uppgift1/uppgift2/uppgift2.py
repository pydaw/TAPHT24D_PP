__solution__ = "1f"

if __solution__ == "1a":
    class Country:
        def __init__(self, name, pop):
            self.__name = name
            self.__population = pop

    se = Country("Sverige", 10.5)
    no = Country("Norge", 5.5)

    # Skapar objekt för Island och Danmark
    isl = Country("Island", 0.4)
    dk = Country("Danmark", 6.0)


elif __solution__ == "1b":
    class Country:
        def __init__(self, name, pop):
            self.__name = name
            self.__population = pop

        def print_info(self):
            print(f"I {self.__name} bor det {self.__population} miljoner invånare")

    se = Country("Sverige", 10.5)
    no = Country("Norge", 5.5)

    # Skapar objekt för Island och Danmark
    isl = Country("Island", 0.4)
    dk = Country("Danmark", 6.0)

    # Testar metoden
    dk.print_info()


elif __solution__ == "1c":
    class Country:
        def __init__(self, name, pop, area = None):
            self.__name = name
            self.__population = pop
            self.__area = area

        def print_info(self):
            print(f"I {self.__name} bor det {self.__population} miljoner invånare")

    se = Country("Sverige", 10.5)
    no = Country("Norge", 5.5)

    # Skapar objekt för Island och Danmark
    isl = Country("Island", 0.4)
    dk = Country("Danmark", 6.0)


elif __solution__ == "1d":
    class Country:
        def __init__(self, name, pop, area = None):
            self.__name = name
            self.__population = pop
            self.__area = area
            
        def print_info(self):
            if self.__area is None:
                print(f"I {self.__name} bor det {self.__population} miljoner invånare")
            else:
                print(f"I {self.__name} bor det {self.__population} miljoner invånare, arean är {self.__area}km²")


    se = Country("Sverige", 10.5, 447425)
    no = Country("Norge", 5.5, 385207)
    isl = Country("Island", 0.4, 103000)
    dk = Country("Danmark", 6.0)

    # Testar metoden
    se.print_info()
    dk.print_info()


elif __solution__ == "1e":
    class Country:
        
        def __init__(self, name, pop, area = None):
            self.__name = name
            self.__population = pop
            self.__area = area
            self.__languages = list()
            
        def print_info(self):
            if self.__area is None:
                print(f"I {self.__name} bor det {self.__population} miljoner invånare")
            else:
                print(f"I {self.__name} bor det {self.__population} miljoner invånare, arean är {self.__area}km²")

        def add_language(self, language):
            self.__languages.append(language)


    se = Country("Sverige", 10.5, 447425)
    no = Country("Norge", 5.5, 385207)
    isl = Country("Island", 0.4, 103000)
    dk = Country("Danmark", 6.0)

    # Testar metoden
    se.print_info()
    dk.print_info()


elif __solution__ == "1f":
    class Country:
        
        def __init__(self, name, pop, area = None):
            self.__name = name
            self.__population = pop
            self.__area = area
            self.__languages = list()
            
        def print_info(self):
            if self.__area is None:
                print(f"I {self.__name} bor det {self.__population} miljoner invånare")
            else:
                print(f"I {self.__name} bor det {self.__population} miljoner invånare, arean är {self.__area}km²")
            
            official_languages = str()
            for language in self.__languages: official_languages = official_languages + f"{language} "
            print(f"Officiella språk för landet är: {official_languages}")

        def add_language(self, language):
            self.__languages.append(language)


    se = Country("Sverige", 10.5, 447425)
    no = Country("Norge", 5.5, 385207)
    isl = Country("Island", 0.4, 103000)
    dk = Country("Danmark", 6.0)
    fi = Country("Finland", 5.6, 338462)
    ch = Country("Schweiz", 8.9, 41285)


    # Testar metoden add_language
    se.add_language("Svenska")

    fi.add_language("Finska")
    fi.add_language("Svenska")
    
    ch.add_language("Tyska")
    ch.add_language("Franska")
    ch.add_language("Italienska")
    ch.add_language("Rätoromanska")
    

    # Testar metoden print_info
    se.print_info()
    dk.print_info()  # Kontrollerar tom lista
    fi.print_info()
    ch.print_info()