answer = -1


def solution(k, dungeons):
    global answer
    visited = [False for _ in range(len(dungeons))]

    def dfs(hp, count):
        global answer

        for i in range(len(dungeons)):
            if visited[i] == False:
                current_dungeon = dungeons[i]
                if hp >= current_dungeon[0]:
                    visited[i] = True
                    dfs(hp - current_dungeon[1], count + 1)
                    visited[i] = False

        answer = max(answer, count)

    dfs(k, 0)

    return answer
