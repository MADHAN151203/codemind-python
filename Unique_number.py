s=int(input())
l=[]
c=1
while s>0:
    r=s%10
    if r in l:
        print("Not Unique Number")
        c=0
        break
    l.append(r)
    s=s//10
if c==1:
    print("Unique Number")
    