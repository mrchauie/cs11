def check_div_3(number):
    if number % 3 == 0:
        return True
    else:
        return False

def check_div_5(number):
    if number % 5 == 0:
        return True
    else:
        return False

def check_div_15(number):
    if number % 15 == 0:
        return True
    else:
        return False

for i in range(1000):
    if check_div_15(i) == True:
        print('fizzbuzz')
    elif check_div_5(i) == True:
        print('buzz')
    elif check_div_3(i) == True:
        print('fizz')    
    else:
        print(i)