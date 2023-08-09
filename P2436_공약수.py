import math
g, l = map(int, input().split())
c = l//g
for i in range(int(c**0.5)):
    if c % (int(c**0.5) - i) == 0 and math.lcm(g * (int(c**0.5) - i), g * c//(int(c**0.5) - i)) == l:
        print(g * (int(c**0.5) - i), g * c//(int(c**0.5) - i))
        break