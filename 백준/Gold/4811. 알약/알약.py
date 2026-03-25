# dp[i][j] = 알약 한 조각이 i개, 반 조각이 j개일 때 문자열 경우의 수
dp = [[0 for _ in range(31)] for _ in range(31)]
dp[0][0] = 1

for i in range(31):
    for j in range(31):
        if j - 1 >= 0:
            dp[i][j] += dp[i][j - 1]
        if i - 1 >= 0 and j + 1 <= 30:
            dp[i][j] += dp[i - 1][j + 1]

while True:
    n = int(input())
    if n == 0:
        break

    print(dp[n][0])
