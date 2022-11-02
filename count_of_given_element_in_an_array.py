a=int(input())
l=list(map(int,input().split()))
n=int(input())
c=0
for i in range(len(l)):
    if n==l[i]:
        c+=1
print(c)