# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    total_slices = x * y
    print((total_slices + 3) // 4)