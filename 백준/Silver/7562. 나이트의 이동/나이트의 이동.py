from collections import deque

t = int(input())

dx = [-1, 1, -1, 1, -2, 2, -2, 2]
dy = [-2, 2, 2, -2, 1, -1, -1, 1]

for _ in range(t):
    l = int(input())
    current_x, current_y = list(map(int, input().split()))
    goal_x, goal_y = list(map(int, input().split()))
    visited = [[False for _ in range(l)] for _ in range(l)]

    queue = deque([(current_x, current_y, 0)])
    visited[current_x][current_y] = True

    def bfs():
        while queue:
            x, y, distance = queue.popleft()
            if x == goal_x and y == goal_y:
                return distance

            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < l and 0 <= ny < l:
                    if visited[nx][ny] == False:
                        visited[nx][ny] = True
                        queue.append((nx, ny, distance + 1))

    print(bfs())
