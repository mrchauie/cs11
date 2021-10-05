n = 100
sum_of_squares = 0
sum_of_series = 0.5 * n * (n + 1)
square_of_sum = sum_of_series * sum_of_series

for i in range(n):
    sum_of_squares = sum_of_squares * sum_of_squares

difference = square_of_sum - sum_of_squares

print(difference)