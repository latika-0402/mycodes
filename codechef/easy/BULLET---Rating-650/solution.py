# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    i=y//x
    if i<z:
        print(z-i)
    else:print(0)