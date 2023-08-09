a=[tuple(map(int,input().split())) for _ in '...']
print("WHERE IS MY CHICKEN?" if (a[0][0]-a[1][0])*(a[0][1]-a[2][1])==(a[0][1]-a[1][1])*(a[0][0]-a[2][0]) else "WINNER WINNER CHICKEN DINNER!")