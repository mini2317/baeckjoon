c = set(input().split()+input().split())
for k in sorted(sum([[(i, j) for i in c] for j in c], start=[])) : print(*k)