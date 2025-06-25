def solution(brown, yellow):
    answer = []
    karosaerosum = (brown + 4) // 2
    karosaero_candidate = []

    for i in range(1, karosaerosum):
        if i >= karosaerosum - i:
            karosaero_candidate.append((i, karosaerosum - i))

    for x, y in karosaero_candidate:
        if x * y - brown - yellow == 0:
            answer = [x, y]
            break

    return answer
