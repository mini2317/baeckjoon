import math
n = int(input())
page = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
p = 10
for i in range(int(math.log10(n))+1):
    nowDigit = n // (p // 10) % p
    lowDigit = n % p
    for j in range(10):
        page[j] += n // p
    page[j] += lowDigit
    for j in range(1,(n % p) // (p // 10)+1):
        page[j] += p//10
    p *= 10
print(*page)