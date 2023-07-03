n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        l1.append(l[i:j+1])
c=0
for i in l1:
    if sum(i)==k:
        c+=1
print(c)