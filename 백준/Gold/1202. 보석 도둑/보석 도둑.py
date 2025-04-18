import heapq

n, k = map(int, input().split())
jewelry = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

# 보석은 무게 기준 오름차순 정렬
jewelry.sort()
# 가방도 오름차순 정렬
bags.sort()

result = 0
heap = []
j = 0  # 보석 인덱스

for bag in bags:
    # 현재 가방에 담을 수 있는 보석들을 최대 힙에 추가
    while j < n and jewelry[j][0] <= bag:
        heapq.heappush(heap, -jewelry[j][1])  # 가치 기준 최대 힙
        j += 1
    if heap:
        result += -heapq.heappop(heap)

print(result)
