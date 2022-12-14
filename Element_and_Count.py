n=int(input())
l=list(map(int,input().split()))
se = []
for i in l:
    if i not in se:
        se.append(i)
for i in se:
    print(i,l.count(i),end=" ")