# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    print(int((y-x)/z))