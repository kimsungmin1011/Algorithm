answer = 0


def solution(numbers, target):
    global answer

    def dfs(current, number):
        global answer
        if current == len(numbers) - 1:
            if number == target:
                answer += 1
            return

        dfs(current + 1, number + numbers[current + 1])
        dfs(current + 1, number - numbers[current + 1])

    dfs(-1, 0)

    return answer