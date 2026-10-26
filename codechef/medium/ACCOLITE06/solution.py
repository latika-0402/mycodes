# cook your dish here
t=int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total_sum = sum(a)
    
    if total_sum % 2 != 0:
        print("NO")
        continue
        
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    possible = False
    for num in a:
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
        if dp[target]:
            possible = True
            break
            
    if possible:
        print("YES")
    else:
        print("NO")