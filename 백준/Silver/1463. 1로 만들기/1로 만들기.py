n = int(input())
dp = [int(1e9) for _ in range(n + 1)]
dp[1] = 0  # i에서 출발하는 경우의 수

for i in range(1, n):
    if i * 3 <= n:
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    if i * 2 <= n:
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    if i + 1 <= n:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)

print(dp[n])
