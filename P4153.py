import math

x1, y1, r1, x2, y2, r2 = map(float, input().split())

d = math.sqrt( (( x1 - x2 ) ** 2) + (( y1 - y2 ) ** 2) )

def cos(a, b, c):
  return ((b ** 2) + (c ** 2) - (a ** 2)) / (2 * b * c)

def sin(a, b, c):
  return math.sqrt( 1 - ((cos(a, b, c)) ** 2) )

def S(a, b, c):
  return (math.asin(sin(a, b, c)) - cos(a, b, c) * sin(a, b, c)) * (b ** 2)

print('%.3f' % round(S(r1, r2, d) + S(r2, r1, d)*1000/1000))