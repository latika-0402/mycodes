# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    f=max(a,b)
    s=max(c,d)
    print(f+s)