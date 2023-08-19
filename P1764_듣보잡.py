import sys
input=sys.stdin.readline
n,m=map(int,input().split())
l=set(input()[:-1]for i in range(n))
s=set(input()[:-1]for i in range(m))
a=l&s
print(len(a),*sorted(a))