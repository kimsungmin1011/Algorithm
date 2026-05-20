def solution(number, k):
    origin_k = k
    stack = []
    index = 0

    while index < len(number) and k >= 0:
        if not stack:
            stack.append(number[index])
            index += 1

        while index < len(number) and stack[-1] >= number[index]:
            stack.append(number[index])
            index += 1

        if index >= len(number) or k <= 0:
            break

        while k > 0 and stack and number[index] > stack[-1]:
            stack.pop(-1)
            k -= 1

    answer = ("").join(stack) + number[index:]
    if len(answer) > len(number) - origin_k:
        answer = answer[: len(number) - origin_k]
    return answer
