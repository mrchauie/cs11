import random

#global variable
balance = 1400

def check_balance(balance, amount):
    if balance >= amount:
        return True
    else:
        return False

def check_div_10(number):
    if number % 10 == 0:
        return True
    else:
        print('YOU need to withdraw in multiples of 10')
        return False

def withdraw(amount):
    global balance
    if (check_balance(balance, amount) == True) and (check_div_10(amount) == True):
        balance = balance - amount - 0.5
        return True
    else:
        print('not enough money!')
        return False

def display_balance(balance):
    print(f'The balance is {balance}')

amount = random.randint(0, 2000)
withdraw(amount)
display_balance(balance)
