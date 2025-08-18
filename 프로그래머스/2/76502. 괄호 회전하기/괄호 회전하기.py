from collections import deque


def solution(s):
    answer = 0
    queue = deque(s)
    l = len(s)

    for _ in range(l):
        a = queue.popleft()
        queue.append(a)

        c_list = []
        flag = True
        for i in queue:
            if i == "[" or i == "{" or i == "(":
                c_list.append(i)
            else:
                if c_list and (
                    (i == "]" and c_list[-1] == "[")
                    or (i == "}" and c_list[-1] == "{")
                    or (i == ")" and c_list[-1] == "(")
                ):
                    c_list.pop()
                else:
                    flag = False
                    break

        if flag == True and len(c_list) == 0:
            answer += 1

    return answer