# cook your dish here
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if b>a:print(0)
    else:
        required=a-b
        if required%4==0:print(required//4)
        else:print(1+required//4)