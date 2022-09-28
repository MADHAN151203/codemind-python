def reverse(n):
    rev=0
    temp=n
    while n:
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev==temp







n=int(input())
ans=reverse(n)
print(ans)
