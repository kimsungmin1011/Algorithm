def solution(s):
    answer = -1
    s = list(s)

    array = []
    array.append(s[0])

    for i in range(1, len(s)):
        if array and array[-1] == s[i]:
            array.pop()
        else:
            array.append(s[i])

    if array:
        answer = 0
    else:
        answer = 1

    return answer
