s=int(input())
for i in range(s):
    n=input()
    c=0
    for i in n:
        if ord(i)>48 and ord(i)<=58:
            c+=1
            break
    if c==0:
        print("No")
    else:
        print("Yes")