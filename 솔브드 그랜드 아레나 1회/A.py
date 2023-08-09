a=[0]*10
for _ in range(5):
    a[int(input())] += 1
for i in range(10):
    if a[i] % 2 == 1:
        print(i)
        break