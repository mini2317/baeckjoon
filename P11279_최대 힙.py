import heapq
from sys import stdin
def input(): return int(stdin.readline().strip())
heap = []
n = input()
for i in range(n):
    now = input()
    if now == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -now)
