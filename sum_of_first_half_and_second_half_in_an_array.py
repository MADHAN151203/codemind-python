n=int(input())
l=list(map(int,input().split()))
f,s=0,0
f=sum(l[:len(l)//2])
s=sum(l[len(l)//2:])
print(f)
print(s)