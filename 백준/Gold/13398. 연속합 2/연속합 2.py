n = int(input())
number = list(map(int, input().split()))

dp = [[0 for _ in range(2)] for _ in range(n)]
dp[0][0] = number[0]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0] + number[i], number[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + number[i])

max_value = -int(1e9)

for i in range(n):
    for j in range(2):
        if i == 0 and j == 1:
            continue
        max_value = max(max_value, dp[i][j])


print(max_value)
