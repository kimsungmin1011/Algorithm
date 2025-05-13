from collections import deque

n = int(input())
visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]
visited[1][0] = True

queue = deque([(1, 0, 0)])

while queue:
    window, board, time = queue.popleft()

    if window == n:
        print(time)
        break

    if window + board <= n and visited[window + board][board] == False:
        visited[window + board][board] = True
        queue.append((window + board, board, time + 1))

    if visited[window][window] == False:
        visited[window][window] = True
        queue.append((window, window, time + 1))

    if window - 1 >= 0 and visited[window - 1][board] == False:
        visited[window - 1][board] = True
        queue.append((window - 1, board, time + 1))
