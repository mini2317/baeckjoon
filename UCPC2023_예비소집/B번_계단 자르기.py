def count_ways(n, k):
    if k == 0:
        if n == 0:
            return 1
        else:
            return 0
    res = 0
    for i in range(n + 1):
        res += count_ways(n - i, k - 1)
    return res

print(count_ways(1, 2))  # prints 4
