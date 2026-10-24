# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    play=x*y
    breaks=(x-1)//3
    bt=breaks*z
    print(play+bt)