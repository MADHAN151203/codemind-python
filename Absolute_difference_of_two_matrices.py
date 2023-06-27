n=int(input())
m1,m2,m3=[],[],[]
for i in range(n):
    m1.append(list(map(int,input().split())))
for i in range(n):
    m2.append(list(map(int,input().split())))
for i in range(n):
    l=[]
    for j in range(n):
        l.append(abs(m1[i][j]-m2[i][j]))
    m3.append(l)
# for i in range(n):
#     for j in range(n):
#         print(m3[i][j],end=' ')
#     print()
for i in m3:
    print(*i)