M, N = int(input()), int(input())
sum_ = 0
first = -1
for n in range(M, N + 1):
    if int(n**0.5) ** 2 == n:
        sum_ += n
        if first == -1 or n < first:
            first = n
sum_, first = sum_, first
if first == -1:
    print(-1)
else:
    print(sum_)
    print(first)
