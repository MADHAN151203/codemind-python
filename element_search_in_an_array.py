a=int(input())
l=list(map(int,input().split()))
n=int(input())
for i in range(len(l)):
    if n in l:
        print("True")
        break
    else:
        print("False")
        break