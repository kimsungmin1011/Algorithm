import heapq

n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()

for _ in range(m):
    first = heapq.heappop(number)
    second = heapq.heappop(number)
    new = first + second
    heapq.heappush(number, new)
    heapq.heappush(number, new)

print(sum(number))
