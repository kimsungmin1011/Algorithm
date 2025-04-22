def solution(s):
    line = []
    s = s.strip()
    flag = False

    yoso = []
    wonso = []

    # 문자열 파싱
    for i in range(1, len(s) - 1):
        if s[i] == ",":
            if wonso:
                yoso.append(int("".join(wonso[:])))
                wonso = []
            else:
                continue
        elif s[i] == "{":
            flag = True
        elif s[i] == "}":
            yoso.append(int("".join(wonso[:])))
            wonso = []
            flag = False
            line.append(yoso[:])
            yoso = []
        elif flag == True:
            wonso.append(s[i])

    # 길이를 기준으로 정렬
    line = sorted(line, key=lambda x: len(x))
    answer = [line[0][0]]  # 첫 번째 요소의 원소 넣기

    for i in range(len(line)):
        for j in line[i]:
            if j not in answer:  # 현재 원소가 answer에 없다면
                answer.append(j)

    return answer
