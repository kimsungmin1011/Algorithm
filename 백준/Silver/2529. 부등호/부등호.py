n = int(input())

budungho = list(input().split())
visited = [False for _ in range(10)]
answer = []


def dfs(idx, array):
    if idx == n:
        answer.append("".join(array))
        return

    if budungho[idx] == ">":
        for i in range(10):
            if visited[i] == False and i < int(array[idx]):
                visited[i] = True
                dfs(idx + 1, array + [str(i)])
                visited[i] = False

    elif budungho[idx] == "<":
        for i in range(10):
            if visited[i] == False and i > int(array[idx]):
                visited[i] = True
                dfs(idx + 1, array + [str(i)])
                visited[i] = False


for i in range(10):
    visited[i] = True
    dfs(0, [str(i)])
    visited[i] = False

print(max(answer))
print(min(answer))
