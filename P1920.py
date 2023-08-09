input()
A = set(map(int,input().split()))
input()
print('\n'.join(tuple(map(lambda x : str(int(int(x) in A)),input().split()))))