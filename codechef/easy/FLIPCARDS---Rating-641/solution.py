# cook your dish here
t=int(input())
for _ in range(t):
    c,f=map(int,input().split())
    if f==0 or c==f:
        print(0)
    else:print(f)