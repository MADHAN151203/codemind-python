n,m=map(int,input().split())
m1=[]
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
    print(sum(a),end=" ")