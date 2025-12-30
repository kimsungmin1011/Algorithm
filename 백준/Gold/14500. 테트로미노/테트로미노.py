n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

mx = max(map(max, graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for _ in range(m)] for _ in range(n)]

max_value = 0


# ㅗ, ㅜ, ㅏ, ㅓ 탐색용 함수
def fuckyou(x, y):
    a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
    if x + 1 < n and y + 2 < m:
        a = graph[x][y] + graph[x][y + 1] + graph[x][y + 2] + graph[x + 1][y + 1]
    if x - 1 >= 0 and y + 2 < m:
        b = graph[x][y] + graph[x][y + 1] + graph[x][y + 2] + graph[x - 1][y + 1]
    if y - 2 >= 0 and x + 1 < n:
        c = graph[x][y] + graph[x][y - 1] + graph[x][y - 2] + graph[x + 1][y - 1]
    if y - 2 >= 0 and x - 1 >= 0:
        d = graph[x][y] + graph[x][y - 1] + graph[x][y - 2] + graph[x - 1][y - 1]
    if x + 2 < n and y + 1 < m:
        e = graph[x][y] + graph[x + 1][y] + graph[x + 2][y] + graph[x + 1][y + 1]
    if x + 2 < n and y - 1 >= 0:
        f = graph[x][y] + graph[x + 1][y] + graph[x + 2][y] + graph[x + 1][y - 1]
    if x - 2 >= 0 and y + 1 < m:
        g = graph[x][y] + graph[x - 1][y] + graph[x - 2][y] + graph[x - 1][y + 1]
    if x - 2 >= 0 and y - 1 >= 0:
        h = graph[x][y] + graph[x - 1][y] + graph[x - 2][y] + graph[x - 1][y - 1]

    return max(a, b, c, d, e, f, g, h)


def dfs(x, y, z, count):
    global max_value

    # 가지치기
    if z + (4 - count) * mx <= max_value:
        return

    # 종료 조건
    if count == 4:
        max_value = max(max_value, z)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(nx, ny, z + graph[nx][ny], count + 1)
            visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = False
        max_value = max(max_value, fuckyou(i, j))

print(max_value)
