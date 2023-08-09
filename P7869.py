import math

x1, y1, r1, x2, y2, r2 = map(float, input().split())

d = ((x1-x2)**2 + (y1-y2)**2)**0.5

if d > r1 + r2:
  rst = 0
  
elif d <= abs(r1 - r2):
  rst = round(math.pi * min(r1, r2)**2*1000)/1000
  
else:
  cosR1 = (r1**2 + d**2 - r2**2) / (2*d*r1)
  R1 = math.acos(cosR1)
  cosR2 = (r2**2 + d**2 - r1**2) / (2*d*r2)
  R2 = math.acos(cosR2)
  S = ((r1**2) * R1) + ((r2**2) * R2) - (d * math.sin(R1) * r1)
  rst = round(S*1000)/1000
print('%.3f' % rst)

import math
x1, y1, r1, x2, y2, r2 = map(float,input().split())
dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
if dist > r1 + r2:
    rst = 0
elif dist <= abs(r1 - r2):
    rst = math.pi * min(r1, r2) ** 2
else:
    phi = (math.acos((r1**2 + dist**2 - r2**2) / (2 * r1 * dist)))
    theta = (math.acos((r2**2 + dist**2 - r1**2) / (2 * r2 * dist)))
    area1 = r2**2 * theta
    area2 = r1**2 * phi
    area3 = dist * r1 * math.sin(phi)
    rst = round((area1 + area2 - area3)*1000)/1000
print('%.3f' % rst)
