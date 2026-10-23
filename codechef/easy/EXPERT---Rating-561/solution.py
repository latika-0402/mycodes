# cook your dish here
t=int(input())
for _ in range(t):
    t,s=map(int,input().split())
    if (s/t)*100>=50:print('YES')
    else:print('NO')