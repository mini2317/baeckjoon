from math import log10
from sys import stdin
from collections import deque
def getLength(x): return int(log10(x)) + 1
def input(): return stdin.readline().strip()
a, b = map(int, input().split())
if a == b:
    print(1)
    quit()
limitLength = getLength(b)
queue = deque([(a, 1)])
while queue:
    now, cnt = queue.popleft()
    if getLength(now * 2) <= limitLength:
        if now * 2 == b:
            print(cnt + 1)
            quit()
        queue.append((now * 2, cnt + 1))
    if getLength(now * 10 + 1) <= limitLength:
        if now * 10 + 1 == b:
            print(cnt + 1)
            quit()
        queue.append((now * 10 + 1, cnt + 1))
else:
    print(-1)