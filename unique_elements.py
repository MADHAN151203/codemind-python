n=int(input())
l1=[]
l2=list(map(int,input().split()))
for i in l2:
    if i not in l1:
        l1.append(i)
for j in l1:
    print(j,end=" ")