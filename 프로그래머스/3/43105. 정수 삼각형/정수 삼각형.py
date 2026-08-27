def solution(triangle):
    answer = 0
    dp=[[0 for _ in range(len(triangle[-1]))] for _ in range(len(triangle))]
    
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            dp[i][j]=triangle[i][j]
    
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j-1>=0:
                dp[i][j]+=max(dp[i-1][j],dp[i-1][j-1])
            else:
                dp[i][j]+=dp[i-1][j]
                
    return max(dp[-1])