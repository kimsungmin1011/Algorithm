alphabet = ["A", "E", "I", "O", "U"]

current_word = []
total_word = []


def dfs(count):
    if current_word:
        total_word.append("".join(current_word))

    if count == 5:
        return

    for i in range(5):
        current_word.append(alphabet[i])
        dfs(count + 1)
        current_word.pop()


def solution(word):
    answer = 1
    dfs(0)

    for i in total_word:
        if i == word:
            break
        else:
            answer += 1

    return answer
