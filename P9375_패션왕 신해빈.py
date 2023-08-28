from sys import stdin
def input(): return stdin.readline().strip()
for testCase in range(int(input())):
    cloth = {}
    names = []
    for i in range(int(input())):
        a, b = input().split()
        if b in names:
            cloth[b] += 1
        else:
            cloth[b] = 2
            names.append(b)
    mul = 1
    for i in range(len(cloth)):
        mul *= cloth[names[i]]
    print(mul - 1)