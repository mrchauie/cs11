# part2.py
# Author: [YOUR NAME HERE]
#
# This file should contain a Python program which generates a Bank and Account objects to match the state described in the lab spec sheet.

from bank import Bank

def part2():
    """
    Function which creates the state of Banks and Accounts described in the lab spec webpage.
    """


    hsbc = Bank('hsbc')
    for index in range (0,10):
        accountname = 'account' + str(index)
        hsbc.add_account(accountname)
        hsbc.deposit(accountname, index*10)

    bisf = Bank('bisf')
    for index in range(0,10):
        accountname = 'account' + str(index)
        bisf.add_account(accountname)
        bal = hsbc.check_balance(accountname)
        hsbc.withdraw(accountname, bal)
        bisf.deposit(accountname,bal*2)

if __name__ == "__main__":
    part2()
