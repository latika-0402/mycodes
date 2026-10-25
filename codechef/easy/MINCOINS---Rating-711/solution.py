# cook your dish here
# cook your dish here
t = int(input())
while t > 0:
    x = int(input())
    coins = (x // 10) + (x % 10) // 5
    
    if x % 5 != 0:
        print(-1)
    else:
        print(coins)
        
    t -= 1