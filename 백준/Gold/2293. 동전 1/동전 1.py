n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

# dp[i] = i원이 되는 경우의수
dp = [0 for _ in range(k + 1)]
dp[0] = 1

for c in coin:
    for i in range(c, k + 1):
        dp[i] += dp[i - c]

print(dp[k])
