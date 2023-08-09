dp={}
N,K=map(int,input().split())
t=lambda x:bin(x)[2:].zfill(N).replace(*'0(').replace(*'1)')
if N%2:print(t(K))
else:
    n=N//2
    if K>(2**N-1-(4**n-1)//3):print(-1)
    else:
        for i in range(n):
            if i==0:dp[1]={'01'}
            else:
                dp[i+1]=set()
                temp=list(dp[i])
                if i==n-1:
                    for j in range(len(temp)):
                        dp[i+1].add(int(f'0{temp[j]}1',2))
                        dp[i+1].add(int(f'01{temp[j]}',2))
                        dp[i+1].add(int(f'{temp[j]}01',2))
                else:
                    for j in range(len(temp)):
                        dp[i+1].add(f'0{temp[j]}1')
                        dp[i+1].add(f'01{temp[j]}')
                        dp[i+1].add(f'{temp[j]}01')
            print(i)
        print(t(list(set(range(2**N))-dp[n])[K]))