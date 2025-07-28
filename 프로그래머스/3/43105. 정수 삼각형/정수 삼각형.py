def solution(triangle):
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    n = len(triangle)
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
            if j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + triangle[i][j])

    return max(dp[n - 1])
