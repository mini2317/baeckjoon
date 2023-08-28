import sys
def input(): return sys.stdin.readline().strip()
n = int(input())
m = int(input())
i = 0
chain = 0
cnt = 0
s = input()
while i + 2 * n + 1 < m:
    if s[i : 3 + i] == 'IOI':
        chain += 1
        i += 2
        if chain == n:
            chain -= 1
            i += 2
    else:
        i += 1
print(cnt)