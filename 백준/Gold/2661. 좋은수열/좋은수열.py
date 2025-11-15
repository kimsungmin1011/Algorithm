n = int(input())

result = []


def dfs(count, array, value):
    for i in range(len(array)):
        for r in range(1, count // 2 + 1):
            if array[i : i + r] == array[i + r : i + 2 * r]:
                return

    if count == n:
        print(value)
        exit()

    for i in range(1, 4):
        dfs(count + 1, array + [i], value * 10 + i)


dfs(0, [], 0)
