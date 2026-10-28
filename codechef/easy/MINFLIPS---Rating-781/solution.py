# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if n % 2 != 0:
        print(-1)
    else:
        diff = abs(l.count(1) - l.count(-1))
        print(diff // 2)