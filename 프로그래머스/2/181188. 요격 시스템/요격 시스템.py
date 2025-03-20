def solution(targets):
    answer = 0
    targets.sort(key=lambda x: (x[1], x[0]))
    end = 0

    for i in targets:
        if end > i[0]:
            continue
        else:
            end = i[1]
            answer += 1

    return answer


# print(solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]))
