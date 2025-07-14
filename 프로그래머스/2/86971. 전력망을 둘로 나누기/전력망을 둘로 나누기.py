def dfs(graph, visited, node):
    count = 1
    for next in graph[node]:
        if visited[next] == False:
            visited[next] = True
            count += dfs(graph, visited, next)

    return count


def solution(n, wires):
    answer = int(1e9)

    for cut in range(n - 1):
        visited = [False for _ in range(n + 1)]
        graph = [[] for _ in range(n + 1)]

        for i in range(n - 1):
            if i == cut:
                continue
            x, y = wires[i]
            graph[x].append(y)
            graph[y].append(x)

        count_list = []
        for i in range(1, n + 1):
            if visited[i] == False:
                visited[i] = True
                count_list.append(dfs(graph, visited, i))

        answer = min(answer, abs(count_list[0] - count_list[1]))

    return answer
