# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    if n>m:print(abs(n-m)+n)
    else:print(n)