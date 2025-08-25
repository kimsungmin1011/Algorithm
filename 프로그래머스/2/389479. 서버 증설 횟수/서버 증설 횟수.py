def solution(players, m, k):
    answer = 0
    server = [0 for _ in range(24)]

    for i in range(24):
        if players[i] <= server[i] * m + m - 1:
            continue
        else:
            count = 0
            while players[i] > (server[i] + count) * m + m - 1:
                count += 1

            answer += count
            for j in range(k):
                if i + j <= 23:
                    server[i + j] += count

    return answer
