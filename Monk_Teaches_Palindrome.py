for i in range(int(input())):
    n=input()
    if n[::-1]==n and len(n)%2==0:
        print("YES EVEN")
    elif n[::-1]==n and len(n)%2!=0:
        print("YES ODD")
    else:
        print("NO")