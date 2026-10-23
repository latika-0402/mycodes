# cook your dish here
T = int(input())
for _ in range(T):
    X ,Y ,Z = map(int,input().split())
    if (Z/(X * Y))*100 >50:print("Yes")
    else:print("no")