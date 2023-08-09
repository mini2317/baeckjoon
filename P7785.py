now=set()
for i in ['']*int(input()):
    name,q=input().split()
    if q == "enter":
        now.add(name)
    else:
        now.remove(name)
print('\n'.join(sorted(list(now),reverse=True)))