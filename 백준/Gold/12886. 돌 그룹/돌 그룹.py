from collections import deque

a, b, c = map(int, input().split())

queue = deque([(a, b, c)])
visited = {}
visited[str(a) + str(b) + str(c)] = 1


def bfs():
    while queue:
        ca, cb, cc = queue.popleft()

        if ca == cb == cc:
            return 1

        if ca != cb:
            if ca > cb and str(ca - cb) + str(cb + cb) + str(cc) not in visited.keys():
                visited[str(ca - cb) + str(cb + cb) + str(cc)] = 1
                queue.append((ca - cb, cb + cb, cc))
            elif (
                cb > ca and str(ca + ca) + str(cb - ca) + str(cc) not in visited.keys()
            ):
                visited[str(ca + ca) + str(cb - ca) + str(cc)] = 1
                queue.append((ca + ca, cb - ca, cc))

        if ca != cc:
            if ca > cc and str(ca - cc) + str(cb) + str(cc + cc) not in visited.keys():
                visited[str(ca - cc) + str(cb) + str(cc + cc)] = 1
                queue.append((ca - cc, cb, cc + cc))
            elif (
                cc > ca and str(ca + ca) + str(cb) + str(cc - ca) not in visited.keys()
            ):
                visited[str(ca + ca) + str(cb) + str(cc - ca)] = 1
                queue.append((ca + ca, cb, cc - ca))

        if cb != cc:
            if cb > cc and str(ca) + str(cb - cc) + str(cc + cc) not in visited.keys():
                visited[str(ca) + str(cb - cc) + str(cc + cc)] = 1
                queue.append((ca, cb - cc, cc + cc))
            elif (
                cc > cb and str(ca) + str(cb + cb) + str(cc - cb) not in visited.keys()
            ):
                visited[str(ca) + str(cb + cb) + str(cc - cb)] = 1
                queue.append((ca, cb + cb, cc - cb))

    return 0


print(bfs())
