import copy, sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    graph = []

    for i in range(3):
        graph.append(list(input().strip()))

    # 보드 형태 변경 (흰색 1, 검은색 -1)
    final_board = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for i2 in range(3):
            if graph[i][i2] == "*":
                final_board[i][i2] = -1
            else:
                final_board[i][i2] = 1

    # 보드 초기 형태 (모두 흰색인 보드)
    start_board = [[1 for _ in range(3)] for _ in range(3)]

    # 5방향 정의
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    def bfs():
        queue = deque([(start_board, 0)])
        visited = set()
        # 2차원 리스트를 튜플로 변환하여 저장
        visited.add(tuple(map(tuple, start_board)))

        while queue:
            array, count = queue.popleft()

            if array == final_board:
                return count

            for i in range(3):
                for i2 in range(3):
                    copyarray = copy.deepcopy(array)  # 현재 보드에 영향 X

                    # 클릭한 칸과 그 칸에 인접한 동서남북 네 칸 색 변경
                    for i3 in range(5):
                        nx, ny = i + dx[i3], i2 + dy[i3]
                        if 0 <= nx < 3 and 0 <= ny < 3:
                            copyarray[nx][ny] = array[nx][ny] * -1

                    # 새로운 상태를 튜플로 변환
                    new_tuple = tuple(map(tuple, copyarray))
                    if new_tuple not in visited:
                        visited.add(new_tuple)
                        queue.append((copyarray, count + 1))

    print(bfs())
