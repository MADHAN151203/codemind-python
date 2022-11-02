a=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    c+=l[i]
avg=c//len(l)
if avg in l:
    print("True")
else:
    print("False")