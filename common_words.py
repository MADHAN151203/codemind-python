s1=input().lower().split()
s2=input().lower().split()
for i in range(0,len(s2)):
    if s2[i] in s1:
        print(s2[i],end=' ')