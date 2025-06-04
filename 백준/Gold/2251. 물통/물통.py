import sys
from collections import deque

input = sys.stdin.readline

a, b, c = map(int, input().split())

queue = deque([(0, 0, c)])
visited = set()
visited.add((0, 0, c))
answer = set()

while queue:
    x, y, z = queue.popleft()
    if x == 0:
        answer.add(z)

    # X => Y
    if (max(0, x - (b - y)), min(b, y + (x - max(0, x - (b - y)))), z) not in visited:
        visited.add((max(0, x - (b - y)), min(b, y + (x - max(0, x - (b - y)))), z))
        queue.append((max(0, x - (b - y)), min(b, y + (x - max(0, x - (b - y)))), z))
    # Y => X
    if (min(a, x + (y - max(0, y - (a - x)))), max(0, y - (a - x)), z) not in visited:
        visited.add((min(a, x + (y - max(0, y - (a - x)))), max(0, y - (a - x)), z))
        queue.append((min(a, x + (y - max(0, y - (a - x)))), max(0, y - (a - x)), z))

    # X => Z
    if (max(0, x - (c - z)), y, min(c, z + (x - max(0, x - (c - z))))) not in visited:
        visited.add((max(0, x - (c - z)), y, min(c, z + (x - max(0, x - (c - z))))))
        queue.append((max(0, x - (c - z)), y, min(c, z + (x - max(0, x - (c - z))))))
    # Z => X
    if (min(a, x + (z - max(0, z - (a - x)))), y, max(0, z - (a - x))) not in visited:
        visited.add((min(a, x + (z - max(0, z - (a - x)))), y, max(0, z - (a - x))))
        queue.append((min(a, x + (z - max(0, z - (a - x)))), y, max(0, z - (a - x))))

    # Z => Y
    if (x, min(b, y + (z - max(0, z - (b - y)))), max(0, z - (b - y))) not in visited:
        visited.add((x, min(b, y + (z - max(0, z - (b - y)))), max(0, z - (b - y))))
        queue.append((x, min(b, y + (z - max(0, z - (b - y)))), max(0, z - (b - y))))
    # Y => Z
    if (x, max(0, y - (c - z)), min(c, z + (y - max(0, y - (c - z))))) not in visited:
        visited.add((x, max(0, y - (c - z)), min(c, z + (y - max(0, y - (c - z))))))
        queue.append((x, max(0, y - (c - z)), min(c, z + (y - max(0, y - (c - z))))))

print(*sorted(list(answer)))
