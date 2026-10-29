t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    print((n-(n//3))*x)
    