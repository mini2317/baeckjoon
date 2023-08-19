from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
arr = deque(int(input()) for _ in range(n))
stack = deque()
comm = []
for i in range(1, n + 1):
    stack.append(i)
    comm.append('+')
    while stack:
        if stack[-1] != arr[0]: break
        stack.pop()
        arr.popleft()
        comm.append('-')
if stack:
    print('NO')
else:
    print(*comm)