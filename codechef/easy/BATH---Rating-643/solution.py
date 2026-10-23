# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    required=2*y
    if 2*y<=x:
        print(x//(required))
    else:print(0)