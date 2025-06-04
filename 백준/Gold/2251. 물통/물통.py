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

    # 1) X => Y
    move = min(x, b - y)
    new_x, new_y, new_z = x - move, y + move, z
    if (new_x, new_y, new_z) not in visited:
        visited.add((new_x, new_y, new_z))
        queue.append((new_x, new_y, new_z))

    # 2) Y => X
    move = min(y, a - x)
    new_x, new_y, new_z = x + move, y - move, z
    if (new_x, new_y, new_z) not in visited:
        visited.add((new_x, new_y, new_z))
        queue.append((new_x, new_y, new_z))

    # 3) X => Z
    move = min(x, c - z)
    new_x, new_y, new_z = x - move, y, z + move
    if (new_x, new_y, new_z) not in visited:
        visited.add((new_x, new_y, new_z))
        queue.append((new_x, new_y, new_z))

    # 4) Z => X
    move = min(z, a - x)
    new_x, new_y, new_z = x + move, y, z - move
    if (new_x, new_y, new_z) not in visited:
        visited.add((new_x, new_y, new_z))
        queue.append((new_x, new_y, new_z))

    # 5) Z => Y
    move = min(z, b - y)
    new_x, new_y, new_z = x, y + move, z - move
    if (new_x, new_y, new_z) not in visited:
        visited.add((new_x, new_y, new_z))
        queue.append((new_x, new_y, new_z))

    # 6) Y => Z
    move = min(y, c - z)
    new_x, new_y, new_z = x, y - move, z + move
    if (new_x, new_y, new_z) not in visited:
        visited.add((new_x, new_y, new_z))
        queue.append((new_x, new_y, new_z))

print(*sorted(list(answer)))
