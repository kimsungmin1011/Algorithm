n = int(input())
m = int(input())

vip = []
for _ in range(m):
    vip.append(int(input()))

# dp[i][j] = i번째 자리에 j번째 사람이 앉는 경우의 수
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
dp[1][1] = 1
if n >= 2 and 2 not in vip:
    dp[1][2] = 1

# 탐색 시작
for i in range(2, n + 1):
    if i - 1 > 0:
        dp[i][i] += sum(dp[i - 1]) - dp[i - 1][i]

    # i가 vip에 없는 경우 i 자리에 i-1, i+1 사람이 들어올 수 있음
    if i not in vip:
        if i - 1 > 0 and i - 1 not in vip:
            dp[i][i - 1] += dp[i - 1][i]
        if i + 1 <= n and i + 1 not in vip:
            dp[i][i + 1] += sum(dp[i - 1]) - dp[i - 1][i]

print(sum(dp[n]))
