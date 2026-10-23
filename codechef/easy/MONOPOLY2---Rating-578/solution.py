# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    profits = list(map(int, input().split()))
    max_profit = max(profits)
    total_profit = sum(profits)
    if max_profit > total_profit - max_profit:
        print("YES")
    else:
        print("NO")