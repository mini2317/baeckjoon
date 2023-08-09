N = int(input())
divided = N
p = N
for i in range(2,int(N ** 0.5) + 1):
    while divided%i == 0:
        divided //= i
        if divided % i != 0:
            p*=(1-(1/i))
if divided != 1:
    p*=(1-(1/divided))
print(int(p))