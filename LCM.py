a,b=map(int,input().split())
t=2
res=1
while a>=t and b>=t:
    if a%t==0 and b%t==0:
        a=a//t
        b=b//t
        res=res*t
    else:
        t+=1
print(res*a*b)
