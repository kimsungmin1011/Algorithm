import math

answer = 0


def sosu(number):
    flag = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            flag = False
            break
    return flag


def solution(nums):
    numbers = []

    def dfs(idx):
        global answer
        if len(numbers) == 3:
            if sosu(sum(numbers)):
                answer += 1
            return

        for i in range(idx, len(nums)):
            numbers.append(nums[i])
            dfs(i + 1)
            numbers.pop()

    dfs(0)

    return answer
