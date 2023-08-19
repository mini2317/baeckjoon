a = int(input())
print(sum(i for i in range(1, a + 1)))
print(sum(i for i in range(1, a + 1))**2)
print(sum(i * i * i for i in range(1, a + 1)))