# cook your dish here
t=int(input())
for _ in range(t):
    n,a,b,c=map(int,input().split())
    if min(a + c, b) >= n:
        print("YES")
    else:
        print("NO")