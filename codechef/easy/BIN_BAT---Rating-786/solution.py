# cook your dish here
import math
t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    power=int(math.log2(n))
    print((a*power)+(b *(power-1)))