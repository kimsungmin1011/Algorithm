def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def dfs(index):
        for j in range(n):
            if computers[index][j] == 1 and visited[j] == False:
                visited[j] = True
                dfs(j)

    for i in range(n):
        if visited[i] == False:
            answer += 1
            visited[i] = True
            dfs(i)

    return answer
