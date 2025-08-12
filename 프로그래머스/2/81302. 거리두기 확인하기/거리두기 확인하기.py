from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(index, a, b, places):
    visited = [[False for _ in range(5)] for _ in range(5)]
    queue = deque([(a, b, 0)])
    visited[a][b] = True

    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == False:
                if places[index][nx][ny] == "X":
                    continue

                elif places[index][nx][ny] == "O":
                    visited[nx][ny] = True
                    queue.append((nx, ny, d + 1))

                elif places[index][nx][ny] == "P":
                    if d + 1 <= 2:
                        return False
                    else:
                        visited[nx][ny] = True
                        queue.append((nx, ny, d + 1))
    return True


def solution(places):
    answer = []
    for index in range(5):
        flag = True
        for i in range(5):
            for j in range(5):
                if places[index][i][j] == "P":
                    if bfs(index, i, j, places) == False:
                        flag = False
                        break

        if flag == True:
            answer.append(1)
        else:
            answer.append(0)

    return answer
