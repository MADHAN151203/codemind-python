n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
for i in l:
    if i>=a and i<=b:
        continue
    else:
        d.append(i)
if len(d)>0:
    print(max(d))
else:
    print("-1")