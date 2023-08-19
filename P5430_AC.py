import sys
from collections import deque
input = sys.stdin.readline
for testCase in range(int(input())):
    q = input()
    n = int(input())
    arr = deque(input()[1:-2].split(','))
    if n == 0: arr = deque()
    error = False
    deleteMod = True
    for i in q:
        if i == 'D':
            if not len(arr):
                error = True
                break
            if deleteMod: arr.popleft()
            else: arr.pop()
        else:
            deleteMod = not deleteMod
    if deleteMod: arr.reverse()
    if error: print('error')
    else: print(f'[{",".join(arr)}]')