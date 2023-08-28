n, m = map(int, input().split())
def make(start, m, info):
    if m > 1:
        for i in range(start, n + 1):
            make(i, m - 1, info + [i])
    else:
        for i in range(start, n + 1):
            print(*(info + [i]))
make(1, m, [])