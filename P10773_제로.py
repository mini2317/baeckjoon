from collections import deque
import sys
input = sys.stdin.readline
sum_ = 0
numbers = deque()
for _ in range(int(input())):
    now = int(input())
    if now == 0:
        sum_ -= numbers.pop()
    else:
        sum_ += now
        numbers.append(now)
print(sum_)