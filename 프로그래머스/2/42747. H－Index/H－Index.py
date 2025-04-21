def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)

    for i in range(max(citations), -1, -1):
        count = 0
        for index in citations:
            if index >= i:
                count += 1
        if count >= i:
            answer = i
            break

    return answer