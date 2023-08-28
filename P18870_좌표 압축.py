import sys
def input(): return sys.stdin.readline().strip()
n = int(input())
x = tuple(map(int, input().split()))
a = sorted(x)
rst = {}
pre = -10000000000
cnt = 0
for i in range(n):
    if a[i] != pre:
        rst[a[i]] = cnt
        cnt += 1
    pre = a[i]
print(*map(lambda x : rst[x], x))