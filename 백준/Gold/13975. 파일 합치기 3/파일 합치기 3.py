import heapq, sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    file = list(map(int, input().split()))
    heapq.heapify(file)
    answer = 0

    while len(file) >= 2:
        first = heapq.heappop(file)
        second = heapq.heappop(file)
        answer += first + second
        heapq.heappush(file, first + second)

    print(answer)
