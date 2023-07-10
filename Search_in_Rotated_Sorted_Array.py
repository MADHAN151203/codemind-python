n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(l)):
    if l[i]==k:
        print(i)
        c=1
if c==0:
    print('-1')