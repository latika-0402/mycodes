# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    result=0
    while n>0:
        rem=n%10
        result=result*10+rem
        n=n//10
    print(result)