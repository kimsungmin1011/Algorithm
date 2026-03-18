n = int(input())
numbers = list(map(int, input().split()))
dp = [[0 for _ in range(21)] for _ in range(n + 1)]
dp[0][numbers[0]] = 1

for i in range(1, n - 1):
    current = numbers[i]
    for j in range(21):
        if 0 <= j - current <= 20:
            dp[i][j] += dp[i - 1][j - current]
        if 0 <= j + current <= 20:
            dp[i][j] += dp[i - 1][j + current]

print(dp[n - 2][numbers[n - 1]])
