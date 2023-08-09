import math, decimal
a, b = map(decimal.Decimal, input().split())
print(int(b * a.log10())+1)