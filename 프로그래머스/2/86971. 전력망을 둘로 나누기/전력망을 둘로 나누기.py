min_diff = int(1e9)


def solution(n, wires):
    global min_diff
    graph = [[] for _ in range(n + 1)]

    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)

    for i in range(len(wires)):
        a, b = wires[i]
        visited = [False for _ in range(n + 1)]

        def dfs(index):
            count = 1
            for next in graph[index]:
                if (index == a and next == b) or (index == b and next == a):
                    continue
                if visited[next] == False:
                    visited[next] = True
                    count += dfs(next)

            return count

        c_count = 0
        flag = 0

        for i2 in range(1, n + 1):
            if visited[i2] == False:
                flag += 1
                visited[i2] = True
                if flag == 1:
                    number = dfs(i2)
                    c_count = number
                elif flag == 2:
                    number = dfs(i2)
                    c_count -= number

        min_diff = min(min_diff, abs(c_count))

    return min_diff
