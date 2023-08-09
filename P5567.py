N,M = int(input()),int(input())
friends = set()
query = []
for _ in '.'*M:
    a = tuple(map(int,input().split()))
    if 1 in a: friends.add(a[1] if a[0]==1 else a[0])
    else: query.append(a)
print(len(set(i[1] if i[0] in friends else i[0] for i in query if (i[0] in friends) or (i[1] in friends)) | friends))