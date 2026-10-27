# cook your dish here
t=int(input())
for _ in range(t):
    a,b,x,y=map(int,input().split())
    if a/x == b/y:
        print("Both")
    elif a/x < b/y :print("Chef")
    else:print("Chefina")