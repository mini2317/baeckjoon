import math
D, H = map(float, input().split())
while True:
    degree = [*map(float, input().split())]
    if any(map(lambda x : x <= 0, degree)): break
    a, b, c = map(lambda x : 1 / math.tan(math.radians(x)), degree)
    rst = 2 * D * D / (a * a + c * c - 2 * b * b)
    print(round(H + math.sqrt(rst)))