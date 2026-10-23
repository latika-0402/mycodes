# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    ratings = list(map(int, input().split()))
    
    # Count how many problems have a rating >= 1000
    remove_count = 0
    for r in ratings:
        if r >= 1000:
            remove_count += 1
            
    print(remove_count)