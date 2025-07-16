def solution(today, terms, privacies):
    answer = []

    today_days = 0
    today = today.split(".")

    for i in range(3):
        if i == 0:
            today_days += 12 * 28 * (int(today[i]) - 1) - 2000
        elif i == 1:
            today_days += 28 * (int(today[i]) - 1)
        else:
            today_days += int(today[i])

    yakkwan = {}
    for term in terms:
        term = term.split(" ")
        yakkwan[term[0]] = int(term[1])

    for i in range(len(privacies)):
        p = privacies[i]
        p = p.replace(".", " ")
        p = p.split(" ")
        current_day = (
            12 * 28 * (int(p[0]) - 1) - 2000 + 28 * (int(p[1]) - 1) + int(p[2])
        )
        if today_days >= current_day + 28 * yakkwan[p[3]]:
            answer.append(i + 1)

    return answer
