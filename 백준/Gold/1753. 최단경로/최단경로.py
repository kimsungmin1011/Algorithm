import heapq

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v)]
distance = [int(1e9) for _ in range(v)]

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))

q = []
distance[k - 1] = 0
heapq.heappush(q, (0, k - 1))

while q:
    d, node = heapq.heappop(q)

    if distance[node] < d:
        continue

    for nx, nd in graph[node]:
        if distance[nx] > d + nd:
            distance[nx] = d + nd
            heapq.heappush(q, (d + nd, nx))

for d in distance:
    if d != int(1e9):
        print(d)
    else:
        print("INF")
