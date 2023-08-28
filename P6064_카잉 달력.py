from math import lcm
import sys
def input(): return sys.stdin.readline().strip()
for testCase in range(int(input())):
    m, n, x, y = map(int, input().split())
    for i in range(x, lcm(m, n) + 1, m):
        a = i % m
        a = a if a else m
        b = i % n
        b = b if b else n
        if a == x and b == y:
            print(i)
            break
    else:
        print(-1)