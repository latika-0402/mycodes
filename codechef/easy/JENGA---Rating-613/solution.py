# cook your dish here
t=int(input())
for _ in range(t):
    N,X=map(int,input().split())
    if N<=X and X%N==0:print("yes")
    else:print("no")