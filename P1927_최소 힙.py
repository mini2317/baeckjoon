import sys
def input(): return sys.stdin.readline().strip()
import heapq
heap = []
for i in range(int(input())):
    n = int(input())
    if n:
        heapq.heappush(heap, n)
    else:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)