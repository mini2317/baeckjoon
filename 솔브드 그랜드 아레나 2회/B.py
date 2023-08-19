a, b, c = input(), input(), input()
q = False
d = 0
try:
    a = int(a)
    q = True
except:
    q = False
if q:
    d = a + 3
else:
    try:
        b = int(b)
        q = True
    except:
        q = False
    if q:
        d = b + 2
    else:
        c = int(c)
        d = c + 1
if d % 3 == 0:
    print('Fizz', end = '')
if d % 5 == 0:
    print('Buzz')
if d % 5 != 0 and d % 3 != 0:
    print(d)
