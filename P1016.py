min_ , max_ = map(int, input().split())
num = [True] * (max_-min_+1)

for i in range(2,int(max_**0.5)+1):
    temp = i**2
    while temp <= max_:
        start = int(min_/temp) * temp
        for j in range(start, max_+1 , temp):
            if j < min_:
                continue
            if num[j-min_]:
                num[j-min_] = False
        temp*=i
print(sum(num))
