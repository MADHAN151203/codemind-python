n=int(input())
ec,dc=0,0
while n>0:
    r=n%10
    if r%2==0:
        ec=1
    else:
        dc=1
    n//=10
if ec==1 and dc==0:
    print("Even")
elif ec==0 and dc==1:
    print("Odd")
else:
    print("Mixed")