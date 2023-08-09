X,Y = 0,1
X,Y,P1,P2 = 0,1,2,3
gcd = lambda a, b : gcd(b, a%b) if b else abs(a)
points = tuple(tuple(map(int,input().split())) for _ in ['']*int(input()))
def getLine(points):
    for i,pnt1 in enumerate(points[:-1]):
        for pnt2 in points[i+1:]:
            x = pnt1[X]-pnt2[X]
            y = pnt1[Y]-pnt2[Y]
            g = gcd(x,y)
            x/=g
            y/=g
            yield x,y,pnt1,pnt2
lines = list(getLine(points))
cnt = 0
for i,line1 in enumerate(lines):
    for line2 in lines[i+1:]:
        cnt += not (line1[X]*line2[X] + line1[Y]*line2[Y]) and (line1[P1] == line2[P1])+(line1[P1] == line2[P2])+(line1[P2] == line2[P1])+(line1[P2] == line2[P2])
print(cnt)