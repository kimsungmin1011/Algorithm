import heapq

# 우선순위 큐 + BFS + 그리디 => 다익스트라
def dijkstra(dist, adj):
    heap = []
    heapq.heappush(heap, [0, 1])  # [누적 비용, 마을 번호]

    while heap:
        cost, node = heapq.heappop(heap)  # 비용이 가장 작은 후보부터 처리

        for c, n in adj[node]:
            if cost + c < dist[n]:  # 더 짧은 경로를 찾으면 갱신
                dist[n] = cost + c
                heapq.heappush(heap, [cost + c, n])


def solution(N, road, K):
    dist = [float('inf')] * (N + 1)  # 1번 마을에서 각 마을까지의 최소 비용
    dist[1] = 0  # 출발점의 비용은 0
    adj = [[] for _ in range(N + 1)]

    for r in road:
        # 양방향 도로를 [이동 비용, 연결된 마을] 형태로 저장
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])

    dijkstra(dist, adj)

    return len([i for i in dist if i <= K])  # K 이하로 배달 가능한 마을 수