# cook your dish here
import math

def solve():
    t = int(input())
    for _ in range(t):
        h, x, y = map(int, input().split())
        remaining_health = h - y
        normal_attacks = math.ceil(remaining_health / x)
        total_with_special = 1 + normal_attacks
        total_normal_only = math.ceil(h / x)
        print(min(total_with_special, total_normal_only))

if __name__ == '__main__':
    solve()