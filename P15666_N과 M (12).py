n, m = map(int, input().split())
given = sorted(map(int, input().split()))
def make(start, info, idx):
    if len(info) != m - 1:
        temp = []
        for i in range(start, n):
            if given[i] in temp: continue
            make(i, info + [given[i]], idx + [i])
            temp.append(given[i])
    else:
        temp = []
        for i in range(start, n):
            if given[i] in temp: continue
            print(*info, given[i])
            temp.append(given[i])
make(0, [], [])