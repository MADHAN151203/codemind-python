n=int(input())
l=list(map(int,input().split()))
l1=[]
sh=l[n//2:]
l1.append(sh[::-1])
#print(l1)
fh=l[:n//2]
l1.append(fh)
for i in l1:
    print(*i,end=' ')