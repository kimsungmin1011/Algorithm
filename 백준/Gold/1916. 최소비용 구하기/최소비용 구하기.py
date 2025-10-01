import heapq

n = int(input())
m = int(input())

distance = [int(1e9) for _ in range(n)]
graph = [[] for _ in range(n)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start - 1].append((end - 1, cost))

s, e = map(int, input().split())
s -= 1
e -= 1

queue = []
heapq.heappush(queue, (0, s))
distance[s] = 0

while queue:
    d, node = heapq.heappop(queue)
    if distance[node] < d:
        continue

    for nn, nc in graph[node]:
        if distance[nn] > d + nc:
            distance[nn] = d + nc
            heapq.heappush(queue, (d + nc, nn))

print(distance[e])
