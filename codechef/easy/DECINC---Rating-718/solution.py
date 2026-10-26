# cook your dish here
t=int(input())
for _ in range(t):
    a,x,b,y=map(int,input().split())
    if a/x == b/y :print("Equal")
    elif a/x > b/y : print("Alice")
    else:print("Bob")