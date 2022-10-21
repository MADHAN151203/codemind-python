n =int(input())
rev,f = 0,0
if n<0:
    n=abs(n)
    f=1
while(n!=0):
	a = n%10
	rev = rev * 10 + a
	n = n // 10
if f==1:
    print(-rev)
else:
    print(rev)
