# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if abs(x-y)<=z:print("YES")
    else:print('NO')
    