n=input()
c=0
for i in n:
    if i>='0' and i<='9':
        c=c+ord(i)-48
print(c)