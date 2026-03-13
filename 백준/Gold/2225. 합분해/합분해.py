import sys

input = sys.stdin.readline

# 0부터 N까지의 정수 K개를 더해서 합이 N이 되는 경우의 수
n, k = map(int, input().split())
# dp[k][n] => 정수 K개를 더해서 합이 N이 되는 경우의 수
dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

# 정수 1개로 i 만드는 경우의 수
for i in range(n + 1):
    dp[1][i] = 1

for i in range(2, k + 1):
    for j in range(n + 1):
        for t in range(j + 1):
            # 정수 i개 더해서 j가 되는 경우의 수 += 정수 i-1개 더해 t가 되는 경우의 수
            # t는 0 ~ 현재값 j
            dp[i][j] += dp[i - 1][t]

print(dp[k][n] % 1000000000)
