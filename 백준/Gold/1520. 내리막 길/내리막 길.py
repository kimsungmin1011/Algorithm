import sys

sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    # 도착 지점에 도달하면 '경로 1개'를 의미
    if x == n - 1 and y == m - 1:
        return 1

    # 이미 계산된 값이 있으면 바로 반환
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0  # 아직 계산 안 된 상태이므로 0으로 초기화

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위 체크 & 내리막(그래프 값이 더 작아야 이동 가능)
        if 0 <= nx < n and 0 <= ny < m:
            if graph[x][y] > graph[nx][ny]:
                # (nx, ny)에서 끝까지 가는 경로 수를 더해줌
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]


answer = dfs(0, 0)
print(answer)
