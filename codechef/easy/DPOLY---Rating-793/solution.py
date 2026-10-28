# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    coeffs = list(map(int, input().split()))
    for i in range(n - 1, -1, -1):
        if coeffs[i] != 0:
            print(i)
            break