import heapq


def solution(operations):
    answer = []

    for i in operations:
        i = list(i.split(" "))
        if i[0] == "I":
            heapq.heappush(answer, int(i[1]))
        else:
            if answer:
                if i[1] == "-1":
                    heapq.heappop(answer)
                elif i[1] == "1":
                    answer.sort()
                    answer.pop()

    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]

