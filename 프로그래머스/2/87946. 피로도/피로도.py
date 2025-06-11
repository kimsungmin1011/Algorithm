answer = -1


def solution(k, dungeons):
    visited = [False for _ in range(len(dungeons))]

    def dfs(hp, count):
        global answer
        answer = max(answer, count)

        for i in range(len(dungeons)):
            if visited[i] == False and hp >= dungeons[i][0]:
                visited[i] = True
                dfs(hp - dungeons[i][1], count + 1)
                visited[i] = False

    dfs(k, 0)

    return answer
