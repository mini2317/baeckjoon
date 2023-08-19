import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dictionary = [input()[:-1] for i in range(n)]
dictionary2 = dict((dictionary[i], i) for i in range(n))
for i in range(m):
    now = input()[:-1]
    try:
        print(dictionary[int(now) - 1])
    except:
        print(dictionary2[now] + 1)