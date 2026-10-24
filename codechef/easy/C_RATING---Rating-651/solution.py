# cook your dish here
# cook your dish here
import math

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    diff = y - x
    print(math.ceil(diff / 8))