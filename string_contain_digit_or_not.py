n=input()
c=0
for i in n:
    if ord(i)>=48 and ord(i)<=57:
        c+=1
if c>1:
    print(f"Contains {c} digit")
else:
    print(f"Doesn't contain digit")