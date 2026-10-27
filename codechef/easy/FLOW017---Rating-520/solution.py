# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    nums=[a,b,c]
    first=second=-1
    for i in nums:
        if i>first:
            second=first
            first=i
        elif i>second:second=i
    print(second)