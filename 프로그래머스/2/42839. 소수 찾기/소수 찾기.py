import math

answer = 0


def sosu(number):
    flag = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            flag = False
            break

    return flag


def solution(numbers):
    numbers = list(numbers)
    visited = [False for _ in range(len(numbers))]
    current_list = []
    jungbok = set()

    def dfs():
        global answer
        if current_list:
            current_nunmber = int("".join(current_list))
        if current_list and current_nunmber > 1:
            if current_nunmber not in jungbok and sosu(current_nunmber):
                jungbok.add(current_nunmber)
                answer += 1

        # if len(current_list) == len(numbers):
        #     return

        for i in range(len(numbers)):
            if visited[i] == False:
                visited[i] = True
                current_list.append(numbers[i])
                dfs()
                current_list.pop()
                visited[i] = False

    dfs()

    return answer
