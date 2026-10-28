# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - 2):
        ans += abs(a[i])
    ans = ans - a[n - 2] + a[n - 1]

    print(ans)
        