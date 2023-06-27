n,m=map(int,input().split())
m1=[]
es,os=0,0
for i in range(n):
    m1.append(list(map(int,input().split())))
for i in range(n):
    if i%2==0:
        es=es+sum(m1[i])
    else:
        os=os+sum(m1[i])
print(es,os)
            