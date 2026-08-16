def solution(n, money):
    answer = 0
    dp=[0 for _ in range(n+1)]
    dp[0]=1
    
    for m in money:
        for i in range(n+1):
            if i-m>=0:
                dp[i]+=dp[i-m] 
    
    answer=dp[n]
    return answer