def check_pronic(n):
    for i in range(n):
        if i * (i + 1) == n:
            return True
        if i * (i + 1) > n:
            return False


num = int(input())
if check_pronic(num):
    print("YES")
else:
    print("NO")
