from collections import deque


def solution(s):
    answer = 0
    queue = deque(s)
    l = len(s)

    for _ in range(l):
        a = queue.popleft()
        queue.append(a)

        c_queue = deque()
        flag = True
        for i in queue:
            if i == "[" or i == "{" or i == "(":
                c_queue.append(i)
            else:
                if c_queue and (
                    (i == "]" and c_queue[-1] == "[")
                    or (i == "}" and c_queue[-1] == "{")
                    or (i == ")" and c_queue[-1] == "(")
                ):
                    c_queue.pop()
                else:
                    flag = False
                    break

        if flag == True and len(c_queue) == 0:
            answer += 1

    return answer