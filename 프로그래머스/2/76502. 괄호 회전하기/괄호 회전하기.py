from collections import deque


def solution(s):
    answer = 0
    count = -1
    queue = deque(s)

    while True:
        count += 1

        if count == len(s):
            break

        flag = True
        check = []

        for i in list(queue):
            if i == "[":
                check.append("[")
            elif i == "]":
                if check and check[-1] == "[":
                    check.pop()
                else:
                    flag = False
                    break

            elif i == "(":
                check.append("(")
            elif i == ")":
                if check and check[-1] == "(":
                    check.pop()
                else:
                    flag = False
                    break

            elif i == "{":
                check.append("{")
            elif i == "}":
                if check and check[-1] == "{":
                    check.pop()
                else:
                    flag = False
                    break

        if len(check) == 0 and flag == True:
            answer += 1

        left = queue.popleft()
        queue.append(left)

    return answer
