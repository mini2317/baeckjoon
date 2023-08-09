x, k = map(int, input().split())
i = 1
xIdx = []
while x != 0:
    if x % 2 == 0: xIdx.append(i)
    i *= 2
    x >>= 1
xIdx.append(i)
i = 0
rst = 0
while k != 0:
    if i < len(xIdx):
        rst += (k % 2) * xIdx[i]
    else:
        rst += k * xIdx[-1] * 2
        break
    i += 1
    k >>= 1
print(rst)