from collections import deque


def solution(maps):
    answer = 0
    maps = [list(i) for i in maps]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                s_x, s_y = i, j
            elif maps[i][j] == "L":
                l_x, l_y = i, j
            elif maps[i][j] == "E":
                e_x, e_y = i, j

    def bfs(a, b, c, d):
        visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
        visited[a][b] = True
        queue = deque([(a, b, 0)])
        flag = False

        while queue:
            x, y, distance = queue.popleft()

            if x == c and y == d:
                flag = True
                return distance

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if visited[nx][ny] == False and maps[nx][ny] != "X":
                        visited[nx][ny] = True
                        queue.append((nx, ny, distance + 1))

        if flag == False:
            return False

    first_length = bfs(s_x, s_y, l_x, l_y)
    if first_length != False:
        answer += first_length
    else:
        return -1

    second_length = bfs(l_x, l_y, e_x, e_y)
    if second_length != False:
        answer += second_length
    else:
        return -1

    return answer