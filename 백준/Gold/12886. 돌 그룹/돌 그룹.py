from collections import deque

a, b, c = map(int, input().split())
visited = set()
visited.add((a, b, c))
queue = deque([(a, b, c)])
flag = False

while queue:
    x, y, z = queue.popleft()
    if x == y == z:
        flag = True
        print(1)
        break

    if x > y:
        if (x - y, y + y, z) not in visited:
            visited.add((x - y, y + y, z))
            queue.append(((x - y, y + y, z)))
    elif x < y:
        if (x + x, y - x, z) not in visited:
            visited.add((x + x, y - x, z))
            queue.append(((x + x, y - x, z)))

    if x > z:
        if (x - z, y, z + z) not in visited:
            visited.add((x - z, y, z + z))
            queue.append(((x - z, y, z + z)))
    elif x < z:
        if (x + x, y, z - x) not in visited:
            visited.add((x + x, y, z - x))
            queue.append(((x + x, y, z - x)))

    if y > z:
        if (x, y - z, z + z) not in visited:
            visited.add((x, y - z, z + z))
            queue.append(((x, y - z, z + z)))
    elif y < z:
        if (x, y + y, z - y) not in visited:
            visited.add((x, y + y, z - y))
            queue.append(((x, y + y, z - y)))

if flag == False:
    print(0)
