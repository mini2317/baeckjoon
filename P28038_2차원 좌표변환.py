import math
for testCase in range(int(input())):
    mod = int(input())
    a, b = map(float, input().split())
    if mod == 1:
        print(math.sqrt(a * a + b * b), (math.atan2(b, a)%(2*math.pi)))
    else:
        print(a * math.cos(b), a * math.sin(b))