n=input()
l=[]
for i in n:
    if ord(i)>48 and ord(i)<=58:
        l.append(int(i))
print(sum(l))