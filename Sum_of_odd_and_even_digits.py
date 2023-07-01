n=int(input())
l=list(map(int,input().split()))
es,os=0,0
for i in range(len(l)):
    if i%2==0:
        es+=l[i]
    elif i%2!=0:
        os+=l[i]
if es-os==0:
    print("YES")
else:
    print("NO")