from collections import deque


def solution(maps):
    answer = []
    graph = []

    for i in maps:
        graph.append(list(i))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]

    def bfs(a, b):
        queue = deque([(a, b)])
        visited[a][b] = True
        count = int(graph[a][b])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                    if graph[nx][ny] != "X" and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        count += int(graph[nx][ny])
        answer.append(count)

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] != "X" and visited[i][j] == False:
                bfs(i, j)

    if answer:
        return sorted(answer)
    else:
        return [-1]
