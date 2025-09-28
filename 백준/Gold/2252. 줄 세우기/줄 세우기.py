from collections import deque

n, m = map(int, input().split())
count = [0 for _ in range(n)]
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    count[b - 1] += 1
    graph[a - 1].append(b - 1)

queue = deque([])

for i in range(n):
    if count[i] == 0:
        queue.append(i)

answer = []

while queue:
    x = queue.popleft()
    answer.append(x + 1)

    for i in graph[x]:
        count[i] -= 1
        if count[i] == 0:
            queue.append(i)

print(*answer)
