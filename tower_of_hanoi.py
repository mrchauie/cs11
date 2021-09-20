def tower_of_hanoi(numbers, start, auxiliary, end):  
    if(numbers == 1):  
        print('Move disk 1 from rod {} to rod {}'.format(start, end))  
        return
    tower_of_hanoi(numbers - 1, start, end, auxiliary)  
    print('Move disk {} from rod {} to rod {}'.format(numbers, start, end))  
    tower_of_hanoi(numbers - 1, auxiliary, start, end)  
   
numbers = 10
tower_of_hanoi(numbers, 'A', 'B', 'C')