def solution(d, budget):
    answer = 0
    d.insert(0,0)
    #dp[x][y] = x번째 부서에 예산 지원 여부에 따라 결정되는 총 지급예산
    dp=[0 for _ in range(len(d))]
    d.sort()
    
    for i in range(1,len(d)):
        if dp[i-1] + d[i] <=budget:
            dp[i] = dp[i-1] + d[i]
            answer+=1
        else:
            dp[i]=dp[i-1]
        
    return answer