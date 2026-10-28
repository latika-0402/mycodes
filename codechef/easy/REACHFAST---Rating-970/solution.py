# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    count=0
    result=[i+k for i in l]
    for i in result:
        if i%7==0:count+=1
    print(count)