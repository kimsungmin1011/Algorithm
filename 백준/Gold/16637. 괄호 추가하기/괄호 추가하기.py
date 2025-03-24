import sys

input = sys.stdin.readline
N = int(input())
words = list(input())
max_value = -int(1e9)


def dfs(i, value):
    global max_value
    # 인덱스가 끝까지 도달한 경우 최댓값 갱신
    if i == N - 1:
        max_value = max(max_value, int(value))
        return

    # 괄호 사용 O
    if i + 4 < N:
        parentheses_value = str(eval("".join(words[i + 2 : i + 5])))
        dfs(i + 4, str(eval("".join([value, words[i + 1], parentheses_value]))))

    # 괄호 사용 X
    if i + 2 < N:
        dfs(i + 2, str(eval("".join([value, words[i + 1], words[i + 2]]))))


dfs(0, words[0])

print(max_value)
