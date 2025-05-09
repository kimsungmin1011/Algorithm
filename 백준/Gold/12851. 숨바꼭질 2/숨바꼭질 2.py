from collections import deque

n, k = map(int, input().split())
visited = [int(1e9) for _ in range(100001)]

queue = deque([])
queue.append(n)

visited[n] = 0
count = 0

while queue:
    current = queue.popleft()
    if current == k:
        count += 1
        continue

    if current - 1 >= 0:
        if visited[current - 1] >= visited[current] + 1:
            visited[current - 1] = visited[current] + 1
            queue.append(current - 1)

    if current + 1 <= 100000:
        if visited[current + 1] >= visited[current] + 1:
            visited[current + 1] = visited[current] + 1
            queue.append(current + 1)

    if current * 2 <= 100000:
        if visited[current * 2] >= visited[current] + 1:
            visited[current * 2] = visited[current] + 1
            queue.append(current * 2)

print(visited[k])
print(count)
