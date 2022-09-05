def tower_of_hanoi(num, start, mid, end):  
    if(num == 1):  
        print('Move disk 1 from rod {} to rod {}'.format(start, end))  
        return
    tower_of_hanoi(num - 1, start, end, mid)  
    print('Move disk {} from rod {} to rod {}'.format(num, start, end))  
    tower_of_hanoi(num - 1, mid, start, end)  
   
num = 5
tower_of_hanoi(num, 'A', 'B', 'C')