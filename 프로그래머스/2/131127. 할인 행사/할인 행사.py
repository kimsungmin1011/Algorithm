import copy


def solution(want, number, discount):
    answer = 0
    want_dict = {}

    for i in range(len(number)):
        want_dict[want[i]] = number[i]

    for i in range(len(discount)):
        new_want_dict = copy.deepcopy(want_dict)
        for j in range(10):
            if i + j < len(discount):
                if discount[i + j] in want_dict and new_want_dict[discount[i + j]] > 0:
                    new_want_dict[discount[i + j]] -= 1

        flag = True
        for i in new_want_dict:
            if new_want_dict[i] > 0:
                flag = False
                break
        if flag == True:
            answer += 1

    return answer
