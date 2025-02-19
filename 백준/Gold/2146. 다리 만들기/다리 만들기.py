from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    queue = deque([(a, b)])
    queue2 = deque([])
    visited2 = [[False for _ in range(n)] for _ in range(n)]  # 0(바다) 방문리스트
    while queue:  # 먼저 현재 섬 탐색
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                if graph[nx][ny] == 0:  # 바다와 맞닿아 있다면
                    queue2.append((x, y, 0))  # 다리 놓기 시작할 후보지

    while queue2:  # 현재 섬 탐색 끝나면 다리 놓기 시작
        x2, y2, t = queue2.popleft()
        for i in range(4):
            nx2, ny2 = x2 + dx[i], y2 + dy[i]
            if 0 <= nx2 < n and 0 <= ny2 < n:
                if graph[nx2][ny2] == 1 and visited[nx2][ny2] == False:
                    return t  # 방문하지 않은 다른 섬과 붙었다면 다리 길이 return

                elif graph[nx2][ny2] == 0 and visited2[nx2][ny2] == False:
                    visited2[nx2][ny2] = True
                    queue2.append((nx2, ny2, t + 1))  # 바다에선 다리 계속 확장

    return int(1e9)  # 모든 섬을 다 방문해서 마지막 섬에서 놓을 다리가 없을 때 return


visited = [[False for _ in range(n)] for _ in range(n)]  # 육지(1) 방문리스트

min_value = int(1e9)
for i in range(n):
    for i2 in range(n):
        if graph[i][i2] == 1 and visited[i][i2] == False:  # 방문하지 않은 섬이 있다면
            visited[i][i2] = True
            # 해당 섬에서 놓을 수 있는 가장 짧은 다리 길이로 최솟값 갱신
            min_value = min(min_value, bfs(i, i2))

print(min_value)
