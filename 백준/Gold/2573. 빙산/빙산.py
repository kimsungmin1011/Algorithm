from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

turn = 0


def bfs(a, b):
    queue = deque([(a, b)])
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and graph[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


while True:
    turn += 1
    queue = deque([])

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                queue.append((i, j))

    this_turn = [[0 for _ in range(m)] for _ in range(n)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] <= 0:
                    this_turn[x][y] += 1

    for i in range(n):
        for j in range(m):
            if this_turn[i][j] > 0:
                graph[i][j] -= this_turn[i][j]

    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and visited[i][j] == False:
                count += 1
                bfs(i, j)

    if count > 1:
        print(turn)
        break
    elif count == 0:
        print(0)
        break
