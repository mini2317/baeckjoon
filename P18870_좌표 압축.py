import sys
def input(): return sys.stdin.readline().strip()
n = int(input())
x = tuple(map(int, input().split()))
a = sorted(x)
before = -10000000000
idx = 0
for i in x:
    if i != before:
        idx = a.index(i)
    print(idx)
    before = i