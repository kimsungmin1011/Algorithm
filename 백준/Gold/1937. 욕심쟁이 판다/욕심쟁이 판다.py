import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# dp[x][y] = (x, y)에서 시작해서 이동할 수 있는 최대 일수(경로 길이)
dp = [[-1 for _ in range(n)] for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    # 이미 계산된 적 있으면 바로 반환 (메모이제이션)
    if dp[x][y] != -1:
        return dp[x][y]

    # 최소 1일(해당 칸에서 시작)
    dp[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[x][y]:
            if dp[nx][ny] == -1:
                dfs(nx, ny)
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)

    return dp[x][y]


answer = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            dfs(i, j)
        answer = max(answer, dp[i][j])

print(answer)
