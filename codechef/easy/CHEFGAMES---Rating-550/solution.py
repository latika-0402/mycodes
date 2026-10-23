# cook your dish here
t = int(input())
for _ in range(t):
    r=list(map(int,input().split()))
    if r.count(1)>0:
        print("OUT")
    else:print("IN")