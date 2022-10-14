import math

n=int(input())
while n>0:
    c=0
    a=int(input())
    for i in range(1,a):
        if i*i==a:
            print("True")
            c=1
    if c==0:
        print("False")
    n-=1