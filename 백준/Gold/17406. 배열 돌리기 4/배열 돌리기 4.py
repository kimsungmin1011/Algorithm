import copy, sys
from itertools import permutations

sys.setrecursionlimit(10**5)

n, m, k = map(int, input().split())
original_graph = []
for _ in range(n):
    original_graph.append(list(map(int, input().split())))

# 각 회전 연산 시작점 및 연산 크기 저장
arr = []
for _ in range(k):
    a, b, c = map(int, input().split())
    arr.append((a - 1, b - 1, c))

# 순열 생성
arr_per = permutations(arr)  # 회전 순서는 임의로 정해도 된다!!!!! (놓친 포인트)

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 회전연산 함수 (좌측상단 (x,y), 우측하단 (ex,ey))
def turn(sx, sy, ex, ey, cx, cy, d, visited, graph, new_graph):
    nx, ny = cx + dx[d], cy + dy[d]
    # 벗어나면 방향 바꾸기
    if (sx <= nx <= ex and sy <= ny <= ey) != True:
        turn(sx, sy, ex, ey, cx, cy, (d + 1) % 4, visited, graph, new_graph)
        return

    # 다 방문했으면 종료
    if visited[nx][ny] == True:
        return

    new_graph[nx][ny] = graph[cx][cy]  # 새 그래프 값 업데이트
    visited[nx][ny] = True  # 방문처리
    turn(sx, sy, ex, ey, nx, ny, d, visited, graph, new_graph)  # 다음으로 이동


answer = int(1e9)

# 각 순열마다 계산 시작
for line in list(arr_per):
    graph = copy.deepcopy(original_graph)
    # 이번 순열에서 순서대로 회전연산 실시
    for x, y, size in line:
        startx, starty = x - size, y - size  # 회전연산 시작점
        endx, endy = x + size, y + size
        new_graph = copy.deepcopy(graph)  # 바뀔 그래프
        visited = [[False for _ in range(m)] for _ in range(n)]  # 방문배열

        # 회전
        i = 0
        while True:
            # 왼쪽 윗칸이 오른쪽 아랫칸 침범하면 종료
            if startx + i >= endx - i and starty + i >= endy - i:
                break

            # 왼쪽상단, 오른쪽하단, 탐색시작좌표, 방향, 방문배열, 새 배열
            turn(
                startx + i,
                starty + i,
                endx - i,
                endy - i,
                startx + i,
                starty + i,
                0,
                visited,
                graph,
                new_graph,
            )
            i += 1

        graph = new_graph

    # 최솟값 갱신
    for line in graph:
        answer = min(answer, sum(line))

print(answer)
