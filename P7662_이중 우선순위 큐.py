import sys
from heapq import *
def input(): return sys.stdin.readline().strip()
for tc in range(int(input())):
    minHeap = []
    maxHeap = []
    cnt = {}
    for k in range(int(input())):
        q, n = input().split()
        n = int(n)
        if q == 'I':
            heappush(minHeap, n)
            heappush(maxHeap, -n)
            if n in cnt: cnt[n] += 1
            else: cnt[n] = 1
        else:
            if n == 1:
                if len(maxHeap) > 0:
                    cnt[- heappop(maxHeap)] -= 1
            else:
                if len(minHeap) > 0:
                    cnt[heappop(minHeap)] -= 1
        i = 0
        while True:
            if not maxHeap: break
            if cnt[- maxHeap[0]] > 0: break
            heappop(maxHeap)
            i += 1
        i = 0
        while True:
            if not minHeap: break
            if cnt[minHeap[0]] > 0: break
            heappop(minHeap)
            i += 1
    if minHeap: print(-heappop(maxHeap), heappop(minHeap))
    else: print('EMPTY')