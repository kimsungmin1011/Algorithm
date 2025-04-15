import heapq

n = int(input())
min_heap = []

for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(min_heap) < n:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

print(min_heap[0])
