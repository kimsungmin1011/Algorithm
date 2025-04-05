max_sheep = 0

def solution(info, edges):
    # 그래프 구성
    n = len(info)
    graph = [[] for _ in range(n)]
    for p, c in edges:
        graph[p].append(c)
        graph[c].append(p)

    # DFS 함수
    #  - index: 현재 노드
    #  - sheep, wolf: 현재까지 방문한 양, 늑대 수
    #  - visited_node: 현재 DFS 경로에서 방문한 노드 집합
    #  - visited: (노드, sheep, wolf) 상태 중복 방문을 막기 위한 집합
    def dfs(index, sheep, wolf, visited_node, visited):
        global max_sheep
        max_sheep = max(max_sheep, sheep)

        for nxt in graph[index]:
            if info[nxt] == 0:  # 양
                # 아직 방문한 적 없는 노드라면
                if nxt not in visited_node:
                    new_visited_node = visited_node | {nxt}
                    # 새 상태 (nxt, sheep+1, wolf)가 처음이라면
                    if (nxt, sheep + 1, wolf) not in visited:
                        new_visited = visited | {(nxt, sheep + 1, wolf)}
                        dfs(nxt, sheep + 1, wolf, new_visited_node, new_visited)
                else:
                    # 이미 방문한 적은 있으나, (nxt, sheep, wolf)는 아직 방문 안 했을 수도
                    if (nxt, sheep, wolf) not in visited:
                        new_visited = visited | {(nxt, sheep, wolf)}
                        dfs(nxt, sheep, wolf, visited_node, new_visited)

            else:  # 늑대
                # 아직 방문한 적 없는 노드라면
                if nxt not in visited_node:
                    # 늑대를 추가해도 양이 더 많아야 진행 가능
                    if sheep > wolf + 1:
                        new_visited_node = visited_node | {nxt}
                        if (nxt, sheep, wolf + 1) not in visited:
                            new_visited = visited | {(nxt, sheep, wolf + 1)}
                            dfs(nxt, sheep, wolf + 1, new_visited_node, new_visited)
                else:
                    if (nxt, sheep, wolf) not in visited:
                        new_visited = visited | {(nxt, sheep, wolf)}
                        dfs(nxt, sheep, wolf, visited_node, new_visited)

    # 루트(0) 노드의 초기값 설정
    initial_sheep = 1 if info[0] == 0 else 0
    initial_wolf = 1 if info[0] == 1 else 0
    
    # DFS 시작
    #  - 방문 상태인 (노드, 양, 늑대)를 visited에 저장
    visited = {(0, initial_sheep, initial_wolf)}
    dfs(0, initial_sheep, initial_wolf, {0}, visited)

    return max_sheep
