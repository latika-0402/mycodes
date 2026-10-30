# cook your dish here
# cook your dish here
t=int(input())
for _ in range(t):
    n, x = map(int, input().split())
    max_rating = 0
    for _ in range(n):
        s, r = map(int, input().split())
        if s <= x and r > max_rating:
            max_rating = r
    print(max_rating)