n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    l1.append(i**2)
print(*sorted(l1))