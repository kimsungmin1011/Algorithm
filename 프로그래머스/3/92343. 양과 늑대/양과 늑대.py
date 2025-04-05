import copy

max_sheep = 0


def solution(info, edges):
    graph = [[] for _ in range(len(info))]

    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    def dfs(index, sheep, wolf, visited_node, visited):
        global max_sheep
        max_sheep = max(max_sheep, sheep)

        for i in graph[index]:
            if info[i] == 0:
                if i not in visited_node:
                    new_visited_node = copy.deepcopy(visited_node)
                    new_visited_node.add(i)
                    new_visited = copy.deepcopy(visited)
                    new_visited.add((i, sheep + 1, wolf))
                    dfs(i, sheep + 1, wolf, new_visited_node, new_visited)
                else:
                    if (i, sheep, wolf) not in visited:
                        new_visited = copy.deepcopy(visited)
                        new_visited.add((i, sheep, wolf))
                        dfs(i, sheep, wolf, visited_node, new_visited)
            else:
                if i not in visited_node:
                    if sheep > wolf + 1:
                        new_visited_node = copy.deepcopy(visited_node)
                        new_visited_node.add(i)
                        new_visited = copy.deepcopy(visited)
                        new_visited.add((i, sheep, wolf + 1))
                        dfs(i, sheep, wolf + 1, new_visited_node, new_visited)
                else:
                    if (i, sheep, wolf) not in visited:
                        new_visited = copy.deepcopy(visited)
                        new_visited.add((i, sheep, wolf))
                        dfs(i, sheep, wolf, visited_node, new_visited)

    v = set()
    v.add((0, 1, 0))
    v_node = set()
    v_node.add(0)

    dfs(0, 1, 0, v_node, v)

    return max_sheep
