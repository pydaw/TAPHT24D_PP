

class BankAccount():

    def __init__(self, savings = 0):
        self.__savings = savings

    def deposit(self, money):
        self.__savings += money

    def withdraw(self, money):
        self.__savings -= money

    def balance(self):
        return self.__savings

    def apply_interest(self, interest = 0.3):
        return self.__savings * (1 + interest)
    
    def afford(self, price):
        return price <= self.__savings
    
    
