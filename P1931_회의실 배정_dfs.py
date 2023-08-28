import sys
from collections import deque
def input(): return sys.stdin.readline().strip()
n = int(input())
timeZone = deque(sorted(sorted([tuple(map(int, input().split())) for _ in range(n)]), key = lambda x : x[1]))
cnt = 0
while timeZone:
    now = timeZone.popleft()
    cnt += 1
    if not timeZone: break
    while timeZone[0][0] < now[1]:
        timeZone.popleft()
        if not timeZone: break
print(cnt)
'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''