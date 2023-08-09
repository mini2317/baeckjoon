N = int(input())
two = N//2 + N//4 + N//8 + N//16 + N//32 + N//64 + N//128 + N//256
five = N//5 + N//25 + N//125
print(min(two,five))