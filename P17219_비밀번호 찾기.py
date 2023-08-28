from sys import stdin
def input(): return stdin.readline().strip()
n, m = map(int, input().split())
siteToPwd = {}
for i in range(n):
    a, b = input().split()
    siteToPwd[a] = b
for i in range(m):
    print(siteToPwd[input()])