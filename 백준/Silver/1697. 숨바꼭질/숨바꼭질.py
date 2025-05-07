from collections import deque

n, k = map(int, input().split())

queue = deque([(n, 0)])
visited = set()
visited.add(n)

while queue:
    node, time = queue.popleft()

    if node == k:
        print(time)
        break

    if node + 1 not in visited and 0 <= node + 1 <= 100000:
        visited.add(node + 1)
        queue.append((node + 1, time + 1))
    if node - 1 not in visited and 0 <= node - 1 <= 100000:
        visited.add(node - 1)
        queue.append((node - 1, time + 1))
    if node * 2 not in visited and 0 <= node * 2 <= 100000:
        visited.add(node * 2)
        queue.append((node * 2, time + 1))
