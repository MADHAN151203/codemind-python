n=int(input())
a=0
b=1
if n==0:
    print("True")
c=a+b
while c<n:
    c=a+b
    a=b
    b=c
if n==c:
    print("True")
else:
    print("False")