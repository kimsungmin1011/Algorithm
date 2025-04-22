answer = int(1e9)


def solution(begin, target, words):
    if target not in words:
        return 0

    word_len = len(words[0])
    visited = [False] * len(words)

    def dfs(current, number):
        global answer
        if current == target:
            answer = min(answer, number)
            return

        for i in range(len(words)):
            if visited[i] == True:
                continue
            count = 0
            for j in range(word_len):
                if current[j] != words[i][j]:
                    count += 1
            if count == 1:
                visited[i] = True
                dfs(words[i], number + 1)
                visited[i] = False

    dfs(begin, 0)

    return answer
