n=int(input())
m=int(input())
n_f=0
for i in range(1,n):
    if n%i==0:
        n_f+=i
m_f=0
for i in range(1,m):
    if m%i==0:
        m_f+=i
if n_f==m and m_f==n:
    print("Amicable")
else:
    print("Not Amicable")



        
        