import heapq

def solution(n, s, a, b, fares):
    answer = int(1e9)
    graph=[[] for _ in range(n+1)]
    for x1,x2,c in fares:
        graph[x1].append((x2,c))
        graph[x2].append((x1,c))
    
    def dijkstra(cs):
        dist=[int(1e9) for _ in range(n+1)]
        dist[cs]=0
        heap = []
        heapq.heappush(heap, [0, cs])  # [누적 비용, 마을 번호]
        while heap:
            cost,node=heapq.heappop(heap)
            for next,sc in graph[node]:
                if cost+sc<dist[next]:
                    dist[next]=cost+sc
                    heapq.heappush(heap, (cost+sc,next))
                    
        return dist[s]+dist[a]+dist[b]
    
    for i in range(1,n+1):
        answer=min(answer,dijkstra(i))
        
    return answer