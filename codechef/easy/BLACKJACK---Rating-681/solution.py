# cook your dish here
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    s=[1,2,3,4,5,6,7,8,9,10]
    j=21-abs(a+b)
    if j in s:
        print(j)
    else:print(-1)