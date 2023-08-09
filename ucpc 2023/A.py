d = 0
for _ in range(10):
    q = input()
    if q == "1":
        d += 1
        d %= 4
    elif q == "2":
        d += 2
        d %= 4
    elif q == "3":
        d -= 1
        if d == -1: d = 3
print('NESW'[d])