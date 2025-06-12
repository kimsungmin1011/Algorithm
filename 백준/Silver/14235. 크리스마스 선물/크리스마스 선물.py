import heapq

n = int(input())

present = []

for i in range(n):
    current = list(map(int, input().split()))
    if current[0] == 0:
        if len(present) == 0:
            print(-1)
        else:
            print(-heapq.heappop(present))

    else:
        for j in range(1, len(current)):
            heapq.heappush(present, -current[j])
