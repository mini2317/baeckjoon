input()
store = {}
for i in map(int,input().split()):
    if store.get(i) is None:
        store[i] = 1
    else:
        store[i] += 1
input()
print(*[0 if store.get(i) is None else store[i] for i in map(int,input().split())])