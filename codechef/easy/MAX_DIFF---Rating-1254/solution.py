# cook your dish here
t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    if s<=n:
        print(s)
    else:print(2*n-s)
        