from collections import deque

n = int(input())
visited = [False for _ in range(n + 1)]
visited[n] = True

queue = deque([(0, [n])])

while queue:
    count, number = queue.popleft()
    lnumber = number[-1]

    if lnumber == 1:
        print(count)
        print(*number)
        break

    if lnumber % 3 == 0 and visited[lnumber // 3] == False:
        visited[lnumber // 3] = True
        queue.append((count + 1, number + [lnumber // 3]))

    if lnumber % 2 == 0 and visited[lnumber // 2] == False:
        visited[lnumber // 2] = True
        queue.append((count + 1, number + [lnumber // 2]))

    if lnumber - 1 >= 0 and visited[lnumber - 1] == False:
        visited[lnumber - 1] = True
        queue.append((count + 1, number + [lnumber - 1]))
