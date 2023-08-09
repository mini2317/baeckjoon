for i in range(int(input())):
    q = list(map(int,input().split()))
    r = sum(q[j] > (sum(q)-q[0])/q[0] for j in range(1,q[0]+1))/q[0]*100
    print(f'{r:.3f}%')