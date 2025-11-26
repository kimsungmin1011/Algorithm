n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[x][y]:
            if dp[nx][ny] == 0:
                dp[nx][ny] = 1
                dfs(nx, ny)
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)


for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            dp[i][j] = 1
            dfs(i, j)

max_value = -1

for i in dp:
    max_value = max(max_value, max(i))

print(max_value)
