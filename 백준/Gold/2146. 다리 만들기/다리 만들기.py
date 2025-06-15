import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited1 = [[False for _ in range(n)] for _ in range(n)]  # 대륙 방문 체크
visited2 = [[int(1e9) for _ in range(n)] for _ in range(n)]  # 바다 방문 체크
min_distance = int(1e9)  # 대륙간 최단거리


# 용도: 같은 육지 탐색해서 모두 방문한 다음 바다와 닿아있는 부분 큐에 넣고 다음 육지까지 탐색
def bfs(a, b):
    global min_distance
    queue1 = deque([(a, b)])
    queue2 = deque()
    visited1[a][b] = True

    # 우선 같은 대륙을 모두 탐색한다
    while queue1:
        x, y = queue1.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited1[nx][ny] == False:
                    if graph[nx][ny] == 1:
                        visited1[nx][ny] = True
                        queue1.append((nx, ny))
                    else:
                        # 바다와 맞닿아 있는 부분은 큐2에 넣어준다
                        queue2.append((x, y, 0))

    # 이후 현재 대륙에서 다른 대륙까지의 거리를 측정한다
    while queue2:
        x, y, distance = queue2.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 and visited2[nx][ny] > distance + 1:
                    # 바다 방문
                    visited2[nx][ny] = distance + 1
                    queue2.append((nx, ny, distance + 1))
                if graph[nx][ny] == 1 and visited1[nx][ny] == False:
                    # 새로운 대륙 방문
                    min_distance = min(min_distance, distance)
                    return


for i in range(n):
    for j in range(n):
        if visited1[i][j] == False and graph[i][j] == 1:
            bfs(i, j)

print(min_distance)
