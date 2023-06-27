n,m=map(int,input().split())
m1=[]
s=0
for i in range(n):
    m1.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        s=s+m1[i][j]
print(s)