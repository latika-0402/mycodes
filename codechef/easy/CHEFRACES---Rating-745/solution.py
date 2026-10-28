# cook your dish here
t=int(input())
for _ in range(t):
    x,y,a,b=map(int,input().split())
    count = 0
    if x != a and x != b:
            count += 1
    
    if y != a and y != b:
            count += 1
    print(count)