import heapq

n, m = map(int, input().split())
card = list(map(int, input().split()))
heapq.heapify(card)

for _ in range(m):
    number1 = heapq.heappop(card)
    number2 = heapq.heappop(card)
    new_number = number1 + number2
    heapq.heappush(card, new_number)
    heapq.heappush(card, new_number)

print(sum(card))
