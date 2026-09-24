import heapq

def solution(n, s, a, b, fares):
    answer = int(1e9)
    graph = [[] for _ in range(n + 1)]

    # 택시 요금은 양방향으로 동일
    for x1, x2, c in fares:
        graph[x1].append((x2, c))
        graph[x2].append((x1, c))

    # via에서 각 지점까지의 최단 요금 계산
    def dijkstra(via):
        dist = [int(1e9) for _ in range(n + 1)]
        dist[via] = 0
        heap = []
        heapq.heappush(heap, [0, via])  # [누적 비용, 지점 번호]

        while heap:
            cost, node = heapq.heappop(heap)
            for next, fare in graph[node]:
                if cost + fare < dist[next]:  # 더 저렴한 경로를 찾으면 갱신
                    dist[next] = cost + fare
                    heapq.heappush(heap, (cost + fare, next))

        # s에서 via까지 합승한 뒤, via에서 a와 b로 각각 이동
        return dist[s] + dist[a] + dist[b]

    # 모든 지점을 합승이 끝나는 지점으로 시도
    for i in range(1, n + 1):
        answer = min(answer, dijkstra(i))

    return answer