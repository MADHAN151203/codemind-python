n,m=map(int,input().split())
m1,m2,m3=[],[],[]
for i in range(n):
    m1.append(list(map(int,input().split())))
for i in range(m):
    l=[]
    for j in range(n):
        l.append(m1[j][i])
    m2.append(l)
for i in m2:
    m3.append(sum(i))
print(max(m3))
        