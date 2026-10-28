# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    curr_max = curr_min = a[-1]

    for i in range(n - 2, -1, -1):
        next_max = max(a[i] - curr_min, curr_max - a[i])
        next_min = min(a[i] - curr_max, curr_min - a[i])
        curr_max, curr_min = next_max, next_min

    print(curr_max)
        