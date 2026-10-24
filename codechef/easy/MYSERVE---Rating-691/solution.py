# cook your dish here
t = int(input())
for _ in range(t):
    p, q = map(int, input().split())
    total_points = p + q
    if (total_points // 2) % 2 == 0:
        print("Alice")
    else:
        print("Bob")