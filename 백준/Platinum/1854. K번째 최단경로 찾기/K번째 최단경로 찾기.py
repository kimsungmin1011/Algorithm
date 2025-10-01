import sys, heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# dist[v]: 정점 v의 "최단거리 후보"를 음수로 저장한 최소힙 (=> 최대힙 효과)
dist = [[] for _ in range(n + 1)]

pq = []
heapq.heappush(pq, (0, 1))
heapq.heappush(dist[1], 0)  # 0의 음수도 0이므로 그대로 push

while pq:
    d, u = heapq.heappop(pq)

    # u의 현재 d가, u가 보유한 K개 후보 중 최악보다도 나쁘면 스킵 가능
    if len(dist[u]) == k and -dist[u][0] < d:
        continue

    for v, w in graph[u]:
        nd = d + w
        if len(dist[v]) < k:
            heapq.heappush(dist[v], -nd)
            heapq.heappush(pq, (nd, v))
        elif -dist[v][0] > nd:  # v가 보유한 최악 후보보다 더 짧으면 교체
            heapq.heapreplace(dist[v], -nd)
            heapq.heappush(pq, (nd, v))

for v in range(1, n + 1):
    if len(dist[v]) < k:
        print(-1)
    else:
        # dist[v]는 음수의 최소힙 → 맨 위는 "가장 큰(=최악) 거리"의 음수
        print(-dist[v][0])