from math import gcd
n = int(input())
arr = list(map(int, input().split()))
print(gcd(*[arr[i] - arr[0] for i in range(1, n)]))