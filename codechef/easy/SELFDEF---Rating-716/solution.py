# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    for i in l:
        if 10<=i<=60:
            count+=1
    print(count)