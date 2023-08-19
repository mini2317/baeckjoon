import sys
def input(): return sys.stdin.readline().strip()
store = {}
for i in range(int(input())):
    q = [*map(int, input().split())]
    if q[0] == 1: store[q[2]] = q[1]
    else: print(store[q[1]])