import sys
input = sys.stdin.readline
n = int(input())
def round(n): return int(n) + (n - int(n) >= 0.5)
r = round(n * 0.15)
a = sorted([int(input()) for _ in range(n)])
if r != 0: a = a[r : - r]
if n != 0:
    print(round(sum(a) / len(a)))
else:
    print(0)