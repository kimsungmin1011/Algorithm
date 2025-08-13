def solution(land):
    answer = 0

    dp = [[0 for _ in range(4)] for _ in range(len(land))]
    for i in range(4):
        dp[0][i] = land[0][i]

    for i in range(1, len(land)):
        for j in range(4):
            for k in range(4):
                if j != k:
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + land[i][j])

    return max(dp[-1])
