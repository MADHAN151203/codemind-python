n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
d=[]
for i in l:
    if i>=a and i<=b:
        d.append(i)
if len(d)>1:
    print(sum(d))
    