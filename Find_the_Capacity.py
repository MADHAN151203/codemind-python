s,t,b=map(int,input().split())
cap=2*s*t*b*512
ans=cap//1024
print(str(ans)+'KB')