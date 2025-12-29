from collections import deque

n, m, t = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

min_answer = int(1e9)


# 시작점에서 종점까지 최단거리 BFS
def bfs():
    global min_answer
    queue = deque([(0, 0, 0)])
    while queue:
        x, y, d = queue.popleft()

        # t시간을 초과하면 넘김
        if d > t:
            continue

        # 걸어서 종점 도착
        if x == n - 1 and y == m - 1:
            min_answer = min(min_answer, d)

        # 칼 먹으면 종점까지 맨해튼(직선) 거리로 계산하기
        if graph[x][y] == 2:
            if t - d >= abs(n - 1 - x) + abs(m - 1 - y):
                min_answer = min(min_answer, d + abs(n - 1 - x) + abs(m - 1 - y))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] != 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, d + 1))

    if min_answer == int(1e9):
        return "Fail"
    else:
        return min_answer


print(bfs())
