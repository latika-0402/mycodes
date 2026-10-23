# cook your dish here
t=int(input())
for _ in range(t):
    b,c=map(int,input().split())
    if b<c:
        print("BIKE")
    elif b>c:
        print("CAR")
    else:print("SAME")