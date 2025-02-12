
from uppgift3 import BankAccount

def test_deposit():
    my_account = BankAccount()
    my_account.deposit(50)
    excepted = 50
    actual = my_account.balance()
    assert actual == excepted


def test_withdraw():
    my_account = BankAccount(50)
    my_account.withdraw(50)
    excepted = 0
    actual = my_account.balance()
    assert actual == excepted


def test_blance():
    my_account = BankAccount(50)
    excepted = 50
    actual = my_account.balance()
    assert actual == excepted


def test_apply_interest():
    my_account = BankAccount(50)
    excepted1 = 65
    actual1 = my_account.apply_interest()
    
    excepted2 = 100
    actual2 = my_account.apply_interest(1)
    
    assert actual1 == excepted1
    assert actual2 == excepted2


def test_afford():
    my_account = BankAccount(50)
    excepted1 = True
    actual1 = my_account.afford(50)
    
    excepted2 = False
    actual2 = my_account.afford(51)
    
    assert actual1 == excepted1
    assert actual2 == excepted2


