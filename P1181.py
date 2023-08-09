a=[set() for i in range(50)]
for i in range(int(input())):
    inp = input()
    a[len(inp)-1].add(inp)
for i in a:
    if a!=set():
        for j in sorted(i):
            print(j)