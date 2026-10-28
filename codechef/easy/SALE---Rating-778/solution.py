# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    sumval=a+max(b,c)
    print(sumval)
    