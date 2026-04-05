import copy, sys
from itertools import permutations

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, k = map(int, input().split())
original_graph = []
for _ in range(n):
    original_graph.append(list(map(int, input().split())))

arr = []
for _ in range(k):
    a, b, c = map(int, input().split())
    arr.append((a - 1, b - 1, c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def rotate(graph, x, y, size):
    startx, starty = x - size, y - size
    endx, endy = x + size, y + size
    new_graph = copy.deepcopy(graph)

    i = 0
    while True:
        sx, sy = startx + i, starty + i
        ex, ey = endx - i, endy - i

        # 더 이상 회전시킬 테두리가 없으면 종료
        if sx >= ex and sy >= ey:
            break

        # 시작점의 값을 before에 저장하고 시계방향으로 한 칸씩 밀어 넣기
        cx, cy = sx, sy
        before = graph[cx][cy]
        d = 0

        while True:
            nx, ny = cx + dx[d], cy + dy[d]

            # 다음 칸이 현재 테두리 범위를 벗어나면 방향 전환
            if not (sx <= nx <= ex and sy <= ny <= ey):
                d = (d + 1) % 4
                continue

            # 다음 칸의 기존 값을 temp에 저장 후, before를 밀어 넣기
            temp = new_graph[nx][ny]
            new_graph[nx][ny] = before
            before = temp

            cx, cy = nx, ny

            # 시작점으로 돌아왔으면 현재 테두리 회전 완료
            if cx == sx and cy == sy:
                break

        i += 1

    return new_graph


answer = int(1e9)

for order in permutations(arr):
    graph = copy.deepcopy(original_graph)

    for x, y, size in order:
        graph = rotate(graph, x, y, size)

    for row in graph:
        answer = min(answer, sum(row))

print(answer)