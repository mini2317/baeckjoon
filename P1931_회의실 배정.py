import sys
from collections import deque
def input(): return sys.stdin.readline().strip()
n = int(input())
timeZone = []
for i in range(n):
    s, e = map(int, input().split())
    if i == 0:
        timeZone.append((s, e))
        continue
    left = 0
    right = i
    while left <= right and left + right < 2 * i:
        mid = (left + right) // 2
        if timeZone[mid][0] < s: left = mid + 1
        else: right = mid - 1
    timeZone.insert(left, (s, e))
max_ = 1
for i in range(n):
    queue = deque([(timeZone.pop(0), 1)])
    while queue:
        now, cnt = queue.popleft()
        left = 0
        right = n - i - 2
        while left <= right:
            mid = (left + right) // 2
            if timeZone[mid][0] >= now[1]: right = mid - 1
            else: left = mid + 1
        for j in range(right + 1, n - i - 1):
            queue.append((timeZone[j], cnt + 1))
            if cnt + 1 > max_: max_ = cnt + 1
print(max_)
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