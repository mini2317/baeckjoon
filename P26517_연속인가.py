k = int(input())
a, b, c, d = map(int, input().split())
print('Yes', a * k + b) if a * k + b == c * k + d else print('No')