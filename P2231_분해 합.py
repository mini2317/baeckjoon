N = int(input())
for i in range(1, 1000000):
    if N == sum(map(int,str(i))) + i:
        print(i)
        break
else : print(0)