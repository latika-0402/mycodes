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
    dp = 1  
    for num in a:
        dp |= (dp << num)
    if (dp >> target) & 1:
        print("YES")
    else:
        print("NO")