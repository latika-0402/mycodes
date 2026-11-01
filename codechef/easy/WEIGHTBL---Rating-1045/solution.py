# cook your dish here
t=int(input())
for _ in range(t):
    w1,w2,x1,x2,m=map(int,input().split())
    actual_gain = w2 - w1
    min_gain = x1 * m
    max_gain = x2 * m
    
    if min_gain <= actual_gain <= max_gain:
        print(1)
    else:
        print(0)