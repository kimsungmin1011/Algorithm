def solution(strs, t):
    INF = 10**9
    n = len(t)
    
    sset = set(strs)              # strs -> set 으로 (O(1) 조회)
    dp = [INF] * (n + 1)
    dp[0] = 0                     # 0 ~ i-1까지 만든 최소 조각 수

    for i in range(1, n + 1):
        # 단어 조각 최대 길이가 5라서 길이 1~5만 확인
        for k in range(1, 6):
            if i - k < 0:
                break
            # t[i-k:i] 가 하나의 후보 조각
            if t[i-k:i] in sset and dp[i-k] != INF:
                if dp[i] > dp[i-k] + 1:
                    dp[i] = dp[i-k] + 1

    return -1 if dp[n] == INF else dp[n]