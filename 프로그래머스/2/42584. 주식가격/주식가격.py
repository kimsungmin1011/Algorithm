def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        current = prices[i]
        count = 1
        for i2 in range(i + 1, len(prices) - 1):
            if prices[i2] >= current:
                count += 1
            else:
                break
        answer.append(count)
    answer.append(0)

    return answer
