# cook your dish here
t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    even_count = n // 2
    odd_count = n - even_count
    total_duration = (even_count * a) + (odd_count * b)
    print(total_duration)