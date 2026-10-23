# cook your dish here
def fact(n):
    if n==0 or n==1:return 1
    return n*fact(n-1)
t=int(input())
for _ in range(t):
    n=int(input())
    print(fact(n))