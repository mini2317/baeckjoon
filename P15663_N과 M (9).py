n, m = map(int, input().split())
given = sorted(map(int, input().split()))
def make(info, idx):
    if len(info) != m - 1:
        temp = []
        for i in range(n):
            if i in idx or given[i] in temp: continue
            make(info + [given[i]], idx + [i])
            temp.append(given[i])
    else:
        temp = []
        for i in range(n):
            if i in idx or given[i] in temp: continue
            print(*info, given[i])
            temp.append(given[i])
make([], [])