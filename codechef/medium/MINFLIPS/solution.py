# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if len(l)%2!=0:
        print(-1)
    else:
        print(abs(l.count(1)-l.count(-1))//2)