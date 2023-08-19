import math
n = int(input())
era = [1, 1] + [0] * (n - 1)
prime = []
for i in range(2, n + 1):
    if era[i] == 0:
        for j in range(i, n + 1, i):
            era[j] = 1
        prime.append(i)
sum_ = 1
for i in prime:
    sum_ = (sum_ * i ** int(math.log(n, i))) % 987654321
print(sum_)