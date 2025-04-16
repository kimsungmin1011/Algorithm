import heapq

queue = []

n = int(input())
answer = 0

for i in range(n):
    heapq.heappush(queue, int(input()))

while len(queue) > 1:
    first = heapq.heappop(queue)
    second = heapq.heappop(queue)
    answer += first + second
    heapq.heappush(queue, first + second)

print(answer)
