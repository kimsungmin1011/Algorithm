def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]

    user = {}
    for i in id_list:
        user[i] = 0

    declaration = {}
    for i in id_list:
        declaration[i] = []

    for i in report:
        i = list(i.split(" "))
        if i[1] not in declaration[i[0]]:
            declaration[i[0]].append(i[1])

    for i in declaration:
        for j in declaration[i]:
            user[j] += 1

    for i in range(len(id_list)):
        for j in declaration[id_list[i]]:
            if user[j] >= k:
                answer[i] += 1

    return answer
