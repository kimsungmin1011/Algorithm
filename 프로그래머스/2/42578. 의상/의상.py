def solution(clothes):
    answer = 1
    fashion = {}

    for i in clothes:
        if i[1] not in fashion:
            fashion[i[1]] = 1
        else:
            fashion[i[1]] += 1

    for i in fashion:
        answer *= fashion[i] + 1

    return answer - 1