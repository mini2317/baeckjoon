import sys, math
from collections import deque
def input(): return sys.stdin.readline().strip()
for tc in range(int(input())):
    a, b = map(int, input().split())
    queue = deque([(a, '')])
    complete = [0] * 10000
    complete[a] = 1
    while queue:
        n, h = queue.popleft()
        d = 2 * n % 10000
        s = (n - 1) % 10000
        l = (n % 1000) * 10 + n // 1000
        r = n // 10 + n % 10 * 1000
        if not complete[d]:
            if d == b:
                print(h + 'D')
                break
            complete[d] = 1
            queue.append((d, h + 'D'))
        if not complete[s]:
            if s == b:
                print(h + 'S')
                break
            complete[s] = 1
            queue.append((s, h + 'S'))
        if not complete[l]:
            if l == b:
                print(h + 'L')
                break
            complete[l] = 1
            queue.append((l, h + 'L'))
        if not complete[r]:
            if r == b:
                print(h + 'R')
                break
            complete[r] = 1
            queue.append((r, h + 'R'))