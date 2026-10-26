# cook your dish here
import math

def solve():
    t = int(input())
    for _ in range(t):
        x, n = map(int, input().split())
        planes_needed = math.ceil(n / 100)
        ans = max(0, planes_needed - x)
        print(ans)

if __name__ == '__main__':
    solve()