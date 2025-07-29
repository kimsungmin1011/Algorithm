t = int(input())


def dfs(index, array1, array2):
    if index == n:
        if eval("".join(array1)) == 0:
            answer.append(array2)
        return

    dfs(index + 1, array1 + [f"+{index+1}"], array2 + f"+{index+1}")
    dfs(index + 1, array1 + [f"-{index+1}"], array2 + f"-{index+1}")
    new_n = array1.pop()
    new_n += str(index + 1)
    dfs(index + 1, array1 + [new_n], array2 + f" {index+1}")


for _ in range(t):
    n = int(input())
    answer = []

    dfs(1, ["1"], "1")

    for i in sorted(answer):
        print(i)
    print()
