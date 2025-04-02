def solution(participant, completion):
    answer = ""
    p_dict = {}
    c_dict = {}

    for i in participant:
        if i not in p_dict:
            p_dict[i] = 1
        else:
            p_dict[i] += 1

    for i in completion:
        if i not in c_dict:
            c_dict[i] = 1
        else:
            c_dict[i] += 1

    for i in p_dict:
        if i not in c_dict or p_dict[i] != c_dict[i]:
            answer = i
            break

    return answer
