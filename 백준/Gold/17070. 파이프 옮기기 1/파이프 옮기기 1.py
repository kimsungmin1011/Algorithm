n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# dp[x][y][방향] = 경우의 수
# 방향: 0 => 가로, 1 => 대각선, 2 => 세로
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            continue

        if j - 1 >= 0:
            dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][1]

        if (
            graph[i - 1][j] == 0
            and graph[i][j - 1] == 0
            and graph[i - 1][j - 1] == 0
            and i - 1 >= 0
            and j - 1 >= 0
        ):
            dp[i][j][1] += (
                dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
            )

        if i - 1 >= 0:
            dp[i][j][2] += dp[i - 1][j][1] + dp[i - 1][j][2]

print(sum(dp[n - 1][n - 1]))
