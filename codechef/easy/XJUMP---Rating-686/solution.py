# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    i=x//y
    if y>x:print(x)
    else:print(((x // y) + (x % y)))