# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    if 1<=n<100:print("Easy")
    elif 100<=n<200:print("Medium")
    else:print("Hard")