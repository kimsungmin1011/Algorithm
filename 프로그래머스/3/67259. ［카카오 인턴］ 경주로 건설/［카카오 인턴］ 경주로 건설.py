from collections import deque

def solution(board):
    n = len(board)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # visited[x][y][방향]: 해당 방향으로 도착하는 최소 비용
    # 방향 0: 세로, 1: 가로
    visited = [[[float('inf')] * 2 for _ in range(n)] for _ in range(n)]
    visited[0][0] = [0, 0]

    # 첫 이동에 코너 비용이 붙지 않도록 두 방향으로 시작
    queue = deque([(0, 0, 0), (0, 0, 1)])

    while queue:
        x, y, direction = queue.popleft()  # direction: 현재 칸에 들어온 방향
        cost = visited[x][y][direction]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                # 이동 번호 0·1(상하) → 세로 0, 2·3(좌우) → 가로 1
                new_direction = i // 2

                # 들어온 방향과 같은 축이면 100원, 꺾으면 600원
                new_cost = cost + (100 if direction == new_direction else 600)

                # 다음 칸에 같은 방향으로 도착하는 비용이 더 저렴하면 갱신
                if new_cost < visited[nx][ny][new_direction]:
                    visited[nx][ny][new_direction] = new_cost
                    queue.append((nx, ny, new_direction))

    return min(visited[n - 1][n - 1])