import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = list(map(int, input().split()))
max_ = max(heap)
heapq.heapify(heap)
dist = max_ - heap[0]
originalDist = max_ - heap[0]
nowMax = max_
while heap[0] <= max_:
    a = heapq.heappop(heap)
    heapq.heappush(heap, a * 2)
    if nowMax - a < dist : dist = nowMax - a
    if nowMax < a * 2: nowMax = a * 2
print(min(dist, originalDist))