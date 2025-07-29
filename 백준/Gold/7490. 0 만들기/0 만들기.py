t = int(input())


def dfs(index, array):
    if index == n:
        if eval(array.replace(" ", "")) == 0:
            answer.append(array)
        return

    dfs(index + 1, array + f"+{index+1}")
    dfs(index + 1, array + f"-{index+1}")
    dfs(index + 1, array + f" {index+1}")


for _ in range(t):
    n = int(input())
    answer = []

    dfs(1, "1")

    for i in sorted(answer):
        print(i)
    print()
