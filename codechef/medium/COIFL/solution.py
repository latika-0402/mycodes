# cook your dish here
def solve():
    S = int(input())
    
    if S == 1:
        print(1)
        return
        
    dp = [0] * (S + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, S + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    print(dp[S])

if __name__ == '__main__':
    solve()