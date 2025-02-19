n = int(input())

result = [0]


def dfs(array, count):
    if len(array) > 0:
        result.append(count)

    for i in range(10):
        if len(array) == 0 or array[-1] > i:
            dfs(array + [i], count * 10 + i)


dfs([], 0)

result.sort()

if len(result) >= n + 1:
    print(result[n])
else:
    print(-1)
