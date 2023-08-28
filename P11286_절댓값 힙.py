import heapq
import sys
def input() : return int(sys.stdin.readline().strip())
positive = []
negative = []
for i in range(input()):
    q = input()
    if q:
        if q < 0:
            heapq.heappush(negative, - q)
        else:
            heapq.heappush(positive, q)
    else:
        if positive and negative:
            if positive[0] < negative[0]:
                print(heapq.heappop(positive))
            else:
                print(- heapq.heappop(negative))
        elif positive:
            print(heapq.heappop(positive))
        elif negative:
            print(- heapq.heappop(negative))
        else:
            print(0)