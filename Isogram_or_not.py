n=input()
c=''
for i in n:
    if i not in c:
        c=c+i
if len(c)==len(n):
    print("True")
else:
    print("False")