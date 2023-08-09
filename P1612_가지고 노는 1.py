N = int(input())
for i in range(1, 1000):
    if int('1' * i) % N == 0:
        print(i)
        break
else:
    print(-1)