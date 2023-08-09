def count_ways(n, last_height=1, num_squares=0):
    if n == 0 and num_squares == n+1:
        return 1
    if n < 0 or num_squares > n+1:
        return 0

    count = 0
    for height in range(last_height, n+2):
        count += count_ways(n-height, height, num_squares+1)

    return count

# Test the function
for i in range(1, 10):
    print(f"The number of ways to divide a staircase of height {i} into {i+1} squares is {count_ways(i)}")
