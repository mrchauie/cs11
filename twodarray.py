board = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

lengthx = len(board)
lengthy = len(board[0])
sum = 0
for y in range(lengthy):
    for x in range(lengthx):
        sum = sum + board[x][y]

print(sum)