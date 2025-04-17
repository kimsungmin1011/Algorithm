from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    document = list(map(int, input().split()))
    queue = deque()

    for i in range(len(document)):
        queue.append((document[i], i))

    count = 1

    while queue:
        current = queue.popleft()
        if len(queue) == 0 or current[0] >= max(i[0] for i in list(queue)):
            if current[1] == m:
                print(count)
                break
            else:
                count += 1
        else:
            queue.append(current)
