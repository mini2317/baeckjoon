N,M = map(int,input().split());
li = [input() for _ in ['']*N]
li2 = [[li[j][i] for j in range(N)] for i in range(M)]
rst = max(sum(not 'X' in li[i] for i in range(N)) , sum(not 'X' in li2[i] for i in range(M)))
print(rst)