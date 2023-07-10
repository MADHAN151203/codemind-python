import math
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if (int(math.log10(i))+1)%2==0:
        c+=1
print(c)
        