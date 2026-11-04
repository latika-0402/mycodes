t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    unique_a = list(set(a))
    unique_a.sort()
    
    print(unique_a[-1] + unique_a[-2])