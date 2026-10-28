# cook your dish here
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if y % x == 0:
        ans = (y // x) - 1
    else:
        ans = y // x
        
    print(max(0, ans))