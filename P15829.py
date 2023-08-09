alphabet = dict(zip('abcdefghijklmnopqrstuvwxyz',range(1,27)))
input()
string = input()
sum_ = 0
def fastPow(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return (fastPow(a,b//2)**2*(a if b % 2 else 1))
for i in range(len(string)) :
    sum_ += alphabet[string[i]] * fastPow(31,i)
print(sum_%1234567891)