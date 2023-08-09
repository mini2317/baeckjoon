import sys
input = sys.stdin.readline
S = set()
r = map(str, range(1,21))
for _ in range(int(input())):
    q = input().split()
    a = q[0][:2]
    if a == 'ad': S.add(q[1])
    elif a == 're': S.remove(q[1]) if q[1] in S else 1
    elif a == 'ch': print(1*(q[1] in S))
    elif a == 'to': S.remove(q[1]) if q[1] in S else S.add(q[1])
    elif a == 'al': S = set(r)
    elif a == 'em': S.clear()