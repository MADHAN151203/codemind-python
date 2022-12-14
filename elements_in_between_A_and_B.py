n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
for i in l:
    if i>=a and i<=b:
        d.append(i)
if len(d)>1:
    print(*d)
else:
    print("-1")
