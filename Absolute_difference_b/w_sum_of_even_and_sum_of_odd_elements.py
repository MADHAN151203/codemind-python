n=int(input())
l=list(map(int,input().split()))
ec=0
oc=0
for i in range(len(l)):
    if l[i]%2!=0:
        oc+=l[i]
    else:
        ec+=l[i]
print(abs(ec-oc))