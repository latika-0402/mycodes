# cook your dish here
t=int(input())
for _ in range(t):
    n,k,m=map(int,input().split())
    print((n + (k * m) - 1) // (k * m))