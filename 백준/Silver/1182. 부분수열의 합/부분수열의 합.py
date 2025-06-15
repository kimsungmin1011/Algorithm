n, s = map(int, input().split())
number = list(map(int, input().split()))
visited = [False for _ in range(len(number))]

answer = 0


def dfs(idx, count, total):
    global answer
    if count > 0 and total == s:
        answer += 1

    for i in range(idx, len(number)):
        if visited[i] == False:
            visited[i] = True
            dfs(i + 1, count + 1, total + number[i])
            visited[i] = False


dfs(0, 0, 0)

print(answer)
