n = int(input())
number = list(map(int, input().split()))
number_list = []
visited = [False for _ in range(n)]

max_answer = -int(1e9)


def dfs(count):
    global max_answer
    if count == n:
        answer = 0
        for i in range(n - 1):
            answer += abs(number_list[i] - number_list[i + 1])
        max_answer = max(max_answer, answer)
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            number_list.append(number[i])
            dfs(count + 1)
            number_list.pop()
            visited[i] = False


dfs(0)

print(max_answer)
