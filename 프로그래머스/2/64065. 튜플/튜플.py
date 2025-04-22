def solution(s):
    answer = []
    s = s.strip()
    flag = False

    imsi = []
    save = []
    for i in range(1, len(s) - 1):
        if s[i] == ",":
            if save:
                imsi.append(int("".join(save[:])))
                save = []
            else:
                continue
        elif s[i] == "{":
            flag = True
        elif s[i] == "}":
            imsi.append(int("".join(save[:])))
            save = []
            flag = False
            answer.append(imsi[:])
            imsi = []
        elif flag == True:
            save.append(s[i])

    answer = sorted(answer, key=lambda x: len(x))
    last = [answer[0][0]]

    for i in range(1, len(answer)):
        for j in answer[i]:
            if j not in last:
                last.append(j)

    return last