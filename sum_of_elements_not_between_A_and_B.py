n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in l:
    if i>=a and i<=b:
        c=c+i
print(sum(l)-c)