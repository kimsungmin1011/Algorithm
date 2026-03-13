n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]

# 합이 0이면, 어떤 k개든 "모두 0"으로 만드는 1가지 방법만 있음
for j in range(1, k + 1):
    dp[0][j] = 1

# 정수 1개만 사용할 때, 합 i를 만드는 방법은 (i) 한 가지 뿐
for i in range(n + 1):
    dp[i][1] = 1


for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[n][k] % 1000000000)
