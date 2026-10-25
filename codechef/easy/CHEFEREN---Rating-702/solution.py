# cook your dish here
t = int(input())
for _ in range(t):
    s, x, y, z = map(int, input().split())
    free_space = s - (x + y)
    
    if free_space >= z:
        print(0)
    elif free_space + x >= z or free_space + y >= z:
        print(1)
    else:
        print(2)