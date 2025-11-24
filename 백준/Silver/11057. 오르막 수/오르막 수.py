n = int(input())

# dp[깊이][마지막 숫자] = 해당 깊이에서 해당 마지막 숫자를 가진 오르막 수의 개수
dp = [[0 for i in range(10)] for _ in range(n)]

# dp 초기값
for i in range(10):
    dp[0][i] += 1

for i in range(1, n):
    for i2 in range(10):
        for i3 in range(i2 + 1):
            # 전 단계에서 마지막 숫자가 i2 이하인 모든 오르막 수의 개수를 더함
            dp[i][i2] += dp[i - 1][i3]

print(sum(dp[n - 1]) % 10007)  # 깊이가 n인 모든 오르막 수의 개수
