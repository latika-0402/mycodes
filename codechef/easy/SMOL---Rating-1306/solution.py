# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 0:
        print(n)
    else:
        print(n % k)