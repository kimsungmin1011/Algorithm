import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []
for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m, v))  # (무게, 가치)

bags = [int(input()) for _ in range(k)]

# 1) 보석을 무게 기준 오름차순 정렬
jewels.sort()

# 2) 가방을 용량 기준 오름차순 정렬
bags.sort()

max_heap = []
idx = 0
answer = 0

# 3) 각 가방에 대해
for capacity in bags:
    #  - 해당 가방에 넣을 수 있는 모든 보석을 max-heap에 추가
    while idx < n and jewels[idx][0] <= capacity:
        # heapq는 최소 힙이므로, 가치에 -를 붙여 최대 힙처럼 사용
        heapq.heappush(max_heap, -jewels[idx][1])
        idx += 1

    #  - 힙에서 가장 가치가 큰 보석을 꺼내어 더함
    if max_heap:
        answer += -heapq.heappop(max_heap)

print(answer)
