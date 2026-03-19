r, c, k = map(int, input().split())
graph = []

for _ in range(r):
    graph.append(list(input()))

visited = [[False for _ in range(c)] for _ in range(r)]
visited[r - 1][0] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0


def dfs(x, y, d):
    global answer
    if d > k:
        return

    if x == 0 and y == c - 1:
        if d == k:
            answer += 1
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] == "T":
                continue
            elif visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny, d + 1)
                visited[nx][ny] = False


dfs(r - 1, 0, 1)

print(answer)
