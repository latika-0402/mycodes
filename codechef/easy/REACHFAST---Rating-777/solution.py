# cook your dish here
import math

def solve():
    t = int(input())
    for _ in range(t):
        a, b, k = map(int, input().split())
        distance = abs(a - b)
        steps = math.ceil(distance / k)
        print(steps)

if __name__ == '__main__':
    solve()
