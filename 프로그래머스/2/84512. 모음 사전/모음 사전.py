moum = ["A", "E", "I", "O", "U"]

array_list = []


def dfs(idx, array):
    if idx == 6:
        return

    array_list.append(array)

    for i in range(5):
        dfs(idx + 1, array + moum[i])


def solution(word):
    for i in range(5):
        dfs(1, moum[i])
    return array_list.index(word) + 1