n,m = map(int,input().split())
m1 = []
for i in range(n):
    m1.append(list(map(int,input().split())))
cnt = 0
for i in range(1,n-1):
    for j in range(1,m-1):
        cnt += m1[i][j]
print(cnt)