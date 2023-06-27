n,m=map(int,input().split())
m1=[]
es,os=0,0
for i in range(n):
    m1.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if m1[i][j]%2:
            os=os+m1[i][j]
        else:
            es=es+m1[i][j]
print(es,os)