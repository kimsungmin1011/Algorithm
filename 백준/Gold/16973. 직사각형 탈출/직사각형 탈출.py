from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

h, w, sr, sc, fr, fc = map(int, input().split())
sr, sc, fr, fc = sr - 1, sc - 1, fr - 1, fc - 1

visited = [[False for _ in range(m - w + 1)] for _ in range(n - h + 1)]
visited[sr][sc] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque([(sr, sc, 0)])
    while queue:
        x, y, time = queue.popleft()
        if x == fr and y == fc:
            return time

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= n - h and 0 <= ny <= m - w and visited[nx][ny] == False:
                flag = True
                if i == 0:
                    for j in range(w):
                        if graph[nx][y + j] == 1:
                            flag = False
                            break

                elif i == 1:
                    for j in range(w):
                        if graph[nx + h - 1][y + j] == 1:
                            flag = False
                            break
                elif i == 2:
                    for j in range(h):
                        if graph[x + j][ny] == 1:
                            flag = False
                            break

                elif i == 3:
                    for j in range(h):
                        if graph[x + j][ny + w - 1] == 1:
                            flag = False
                            break

                if flag == True:
                    visited[nx][ny] = True
                    queue.append((nx, ny, time + 1))

    return -1


print(bfs())
