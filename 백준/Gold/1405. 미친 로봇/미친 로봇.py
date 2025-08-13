probablity = list(map(int, input().split()))

n = probablity.pop(0)
# print(n)

visited = [[False] * (n * 2 + 1) for _ in range(n * 2 + 1)]
visited[n][n] = True

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

hap = 0


def dfs(count, x, y, number):
    global hap
    if number == n:
        hap += count
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(count * (probablity[i] / 100), nx, ny, number + 1)
            visited[nx][ny] = False


dfs(1, n, n, 0)

print(hap)
