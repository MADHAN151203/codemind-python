n,m=map(int,input().split())
m1,m2,m3=[],[],[]
for i in range(n):
    m1.append(list(map(int,input().split())))
for i in range(n):
    l=[]
    for j in range(m):
        l.append(m1[i][j])
    m2.append(l)
for i in m2:
    m3.append(sum(i))
print(max(m3))