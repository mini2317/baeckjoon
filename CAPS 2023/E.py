import sys
def sum_(arr):
    l = len(arr)
    if l == 1: return (arr[0], arr[0])
    elif l == 2: return (arr[0] + arr[1], arr[0] if arr[0] > arr[1] else arr[1])
    else:
        mid = l // 2
        a = sum_(arr[:mid])
        b = sum_(arr[mid:])
        return (a[0] + b[0], a[1] if a[1] > b[1] else b[1])
for _ in range(int(input())):
    N, k = map(int, sys.stdin.readline().split())
    ground = tuple(map(int, sys.stdin.readline().split()))
    for i in range(k):
        i, j = map(int, sys.stdin.readline().split())
        s, b = sum_(ground[i-1 : j])
        print(b * (j - i + 1) - s)
'''
1
7 3
2 1 4 1 2 1 1
3 5
6 7
1 2
'''