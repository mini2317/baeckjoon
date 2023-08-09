astr = 'abcdefghijklnmopqrstuvwxyz'
adict = dict(('abcdefghijklnmopqrstuvwxyz'[i],i) for i in range(26))
ma = dict(('aeiou'[i],[0,4,8,14,20][i]) for i in range(5))
mlist = [0,4,8,14,20]
L,C=map(int,input().split())
txt=list(map(int,input().split()))
txt_num=sorted([adict[txt[i]] for i in range(C)])
