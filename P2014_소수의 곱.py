import heapq
k, n = map(int, input().split())
first = list(map(int, input().split()))
heapq.heapify(first)
i = 1
pre = 0
while i < n:
    now = heapq.heappop(first)
    if now == pre:
        print("?", now)
        heapq.heappush(first, now * 2)
    else:
        print(i, now)
        heapq.heappush(first, now * 2)
        pre = now
        i += 1
print(heapq.heappop(first))