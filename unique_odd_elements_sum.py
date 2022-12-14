n=int(input())
l=list(map(int,input().split()))
c=0
d=[]
for i in l:
    if i not in d:
        d.append(i)
for i in d:
    if i%2:
        c+=i
print(c)
    