# cook your dish here
t=int(input())
for _ in range(t):
    Q,E,H=map(int,input().split())
    if Q<=(E+(H*2)):print("QUALIFY")
    else:print("")