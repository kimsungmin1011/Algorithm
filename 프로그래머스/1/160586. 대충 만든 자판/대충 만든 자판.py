def solution(keymap, targets):
    answer = []
    k_dict = {}

    for key in keymap:
        for i in range(len(key)):
            if key[i] not in k_dict or k_dict[key[i]] > i + 1:
                k_dict[key[i]] = i + 1

    for t in targets:
        number = 0
        flag = True
        for i in t:
            if i in k_dict:
                number += k_dict[i]
            else:
                flag = False
                break
        if flag == True:
            answer.append(number)
        else:
            answer.append(-1)

    return answer
