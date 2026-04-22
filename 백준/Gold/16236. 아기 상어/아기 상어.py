import sys
from collections import deque

input = sys.stdin.readline
# graph 구성 (NxN 크기의 바다)
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 이동 방향 (동, 서, 남, 북)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 최단 거리를 비교할 때 사용할 매우 큰 값 (INF)
INF = 1e9

# 아기 상어의 초기 크기
shark_size = 2

# 아기 상어의 현재 좌표 (초기 위치)
now_x, now_y = 0, 0

# 아기 상어 초기 위치 확인 및 설정
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:  # 9는 아기 상어의 초기 위치를 나타냄
            now_x, now_y = i, j
            graph[i][j] = 0  # 초기 위치를 0으로 변경 (이동 가능한 빈 공간으로 설정)


# 현재 위치에서 각 물고기까지의 거리를 BFS로 계산하는 함수
def BFS():
    queue = deque([(now_x, now_y)])  # BFS 탐색을 위한 큐 (현재 위치에서 시작)
    visited = [[-1] * N for _ in range(N)]  # 방문 여부와 거리를 저장하는 2차원 배열
    visited[now_x][now_y] = 0  # 시작 위치의 거리는 0으로 설정

    while queue:
        x, y = queue.popleft()  # 현재 위치를 큐에서 꺼냄

        for i in range(4):  # 동, 서, 남, 북 네 방향으로 탐색
            nx, ny = x + dx[i], y + dy[i]
            # graph 범위 안에 있고, 아직 방문하지 않았으며 상어가 이동할 수 있는 경우
            if 0 <= nx < N and 0 <= ny < N:
                if shark_size >= graph[nx][ny] and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1  # 이동 거리를 기록
                    queue.append((nx, ny))  # 다음 탐색 위치를 큐에 추가

    return visited  # 모든 위치까지의 거리 정보 반환


# 아기 상어가 먹을 수 있는 물고기를 찾는 함수
def solve(visited):
    x, y = 0, 0  # 먹을 물고기의 좌표
    min_distance = INF  # 가장 가까운 물고기까지의 거리

    for i in range(N):
        for j in range(N):
            # BFS에서 도달할 수 있는 위치이고, 상어가 먹을 수 있는 물고기인 경우
            if visited[i][j] != -1 and 1 <= graph[i][j] < shark_size:
                if visited[i][j] < min_distance:  # 더 가까운 물고기가 있으면 갱신
                    min_distance = visited[i][j]
                    x, y = i, j

    # 만약 먹을 물고기가 없는 경우
    if min_distance == INF:
        return False
    else:
        return x, y, min_distance  # 물고기의 좌표와 거리 반환


answer = 0  # 걸린 시간(총 이동 거리)
food = 0  # 현재 크기에서 먹은 물고기 수

# 시뮬레이션 반복
while True:
    result = solve(BFS())  # BFS로 거리 계산 후 먹을 물고기 찾기

    if not result:  # 먹을 물고기가 없는 경우 종료
        print(answer)
        break
    else:
        now_x, now_y = result[0], result[1]  # 물고기를 먹은 위치로 이동
        answer += result[2]  # 이동한 거리(시간)를 누적
        graph[now_x][now_y] = 0  # 물고기를 먹은 위치를 빈 공간으로 설정
        food += 1  # 먹은 물고기 수 증가

    # 상어의 크기 증가 조건 (먹은 물고기 수가 현재 크기와 같아지면)
    if food >= shark_size:
        shark_size += 1  # 상어의 크기 증가
        food = 0  # 먹은 물고기 수 초기화
