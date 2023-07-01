n,m=map(int,input().split())
m1=[]
for i in range(n):
    m1.append(list(map(int,input().split())))
c=0
for i in range(n):
    for j in range(m):
        if (i==0 or j==0 or i==n-1 or j==m-1):
            c+=m1[i][j]
print(c)