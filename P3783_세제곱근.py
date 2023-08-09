from sys import stdin
import decimal
decimal.getcontext().prec = 160
input = stdin.readline
for _ in range(int(input())):
    n = decimal.Decimal(input())
    x = n
    for i in range(1000):
        x = x - (x * x * x - n)/(3 * x * x)
    num = str(x).split('.')
    if len(num) == 1:
        print(str(x) + '.0000000000')
    else:
        print(num[0] + '.' + num[1][:10])