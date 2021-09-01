'''
this is the offical, complete pseudocode for the sevens game 

loop for NUMBER = 1 to 100
    if NUMBER mod 7 = 0 OR NUMBER contains '7'
        stay silent
    else
        say the number
end loop

'''




# this is a comment
'''
this is a comment block

'''

for number in range(1, 100):
    if number % 7 == 0 or str(number).__contains__('7'):
        print('shhhhhhhh')
    else:
        print(number)


def contains_seven(number_as_string):
    length = len(number_as_string)
    for i in range(length):
        if number_as_string[i] == '7':
            return True
    return False
