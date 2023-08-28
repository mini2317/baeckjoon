n, m = map(int, input().split())
given = sorted(map(int, input().split()))
def make(m, info):
    if m > 1:
        for i in range(n):
            if info:
                if given[i] < info[-1]: continue
            make(m - 1, info + [given[i]])
    else:
        for i in range(n):
            if info:
                if given[i] < info[-1]: continue
            print(*(info + [given[i]]))
make(m, [])