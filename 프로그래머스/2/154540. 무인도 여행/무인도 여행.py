from collections import deque


def solution(maps):
    answer = []
    maps = [list(i) for i in maps]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]

    def bfs(a, b):
        queue = deque([(a, b)])
        total = int(maps[a][b])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if visited[nx][ny] == False and maps[nx][ny] != "X":
                        visited[nx][ny] = True
                        total += int(maps[nx][ny])
                        queue.append((nx, ny))
        return total

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and visited[i][j] == False:
                visited[i][j] = True
                island = bfs(i, j)
                answer.append(island)

    if len(answer) == 0:
        return [-1]
    else:
        return list(sorted(answer))
