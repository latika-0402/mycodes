# cook your dish here
import math

def solve():
    t = int(input())
    for _ in range(t):
        x, y, r = map(int, input().split())
        extra_sticks = r // 30
        total_sticks = x + extra_sticks
        plates = math.ceil(total_sticks / y)
        print(plates)

if __name__ == '__main__':
    solve()