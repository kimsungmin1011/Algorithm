max_sheep = 0


def solution(info, edges):
    graph = [[] for _ in range(len(info))]

    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    def dfs(index, sheep, wolf):
        global max_sheep
        max_sheep = max(max_sheep, sheep)

        for i in graph[index]:
            if info[i] == 0:
                if i not in v_node:
                    v_node.append(i)
                    v.append((i, sheep + 1, wolf))
                    dfs(i, sheep + 1, wolf)
                    v_node.pop()
                    v.pop()
                else:
                    if (i, sheep, wolf) not in v:
                        v.append((i, sheep, wolf))
                        dfs(i, sheep, wolf)
                        v.pop()
            else:
                if i not in v_node:
                    if sheep > wolf + 1:
                        v_node.append(i)
                        v.append((i, sheep, wolf + 1))
                        dfs(i, sheep, wolf + 1)
                        v_node.pop()
                        v.pop()
                else:
                    if (i, sheep, wolf) not in v:
                        v.append((i, sheep, wolf))
                        dfs(i, sheep, wolf)
                        v.pop()

    v = []
    v.append((0, 1, 0))
    v_node = []
    v_node.append(0)

    dfs(0, 1, 0)

    return max_sheep
