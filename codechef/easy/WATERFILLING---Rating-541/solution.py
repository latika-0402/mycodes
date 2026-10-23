# cook your dish here
t=int(input())
for _ in range(t):
    B=list(map(int,input().split()))
    if (B.count(0)>B.count(1)):print("Water filling time")
    else:print("Not now")