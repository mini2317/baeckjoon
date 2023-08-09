A, B = map(int, input().split())
save = []
for i in range(1, int(A**0.5) + 1):
    if A % i == 0:
        save.append(i)
        save.append(A//i)
print(save)