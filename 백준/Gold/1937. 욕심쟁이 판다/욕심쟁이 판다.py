import sys

sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# dp[x][y] : (x, y) 위치에서 시작했을 때 이동할 수 있는 최대 경로 길이
dp = [[-1] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    # 이미 dp[x][y]에 값이 채워져 있다면, (x, y)에서 시작하는 최대 경로 길이를 계산한 적이 있다는 의미
    if dp[x][y] != -1:
        return dp[x][y]

    # dp[x][y]가 -1이면 아직 계산하지 않은 위치이므로, 우선 1로 초기화
    # (자기 자신 위치에서 시작하면 최소 경로 길이는 1)
    dp[x][y] = 1

    # 네 방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 체크 + 다음 칸이 현재 칸보다 값이 클 때만 이동 가능
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > graph[x][y]:
                # (nx, ny)에서 시작하는 최대 경로 길이를 dfs로 구해서 + 1
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


max_value = 0
for i in range(n):
    for j in range(n):
        # 모든 칸에 대해 dfs를 수행하고, 그 결과(최대 경로 길이)를 갱신
        max_value = max(max_value, dfs(i, j))

print(max_value)
