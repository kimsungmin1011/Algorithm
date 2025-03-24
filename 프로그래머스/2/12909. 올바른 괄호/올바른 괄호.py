def solution(s):
    answer = True

    s = list(s)
    count = 0

    for i in s:
        if i == "(":
            count += 1

        elif i == ")":
            count -= 1

        if count < 0:
            answer = False
            break

    if count != 0:
        answer = False

    return answer
