from collections import deque

answer = 0


def solution(begin, target, words):
    global answer
    if target not in words:
        return 0

    word_len = len(words[0])
    visited = [False] * len(words)
    queue = deque()
    queue.append((begin, 0))

    def bfs():
        global answer
        while queue:
            node, count = queue.popleft()
            if node == target:
                answer = count
                return

            for i in range(len(words)):
                if visited[i] == True:
                    continue

                diff = 0
                for j in range(word_len):
                    if node[j] != words[i][j]:
                        diff += 1

                if diff == 1:
                    visited[i] = True
                    queue.append((words[i], count + 1))

    bfs()

    return answer