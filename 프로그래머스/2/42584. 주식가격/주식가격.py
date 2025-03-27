def solution(prices):
    answer = []

    for i in range(len(prices)):
        current = prices[i]
        count = 0
        for i2 in range(i + 1, len(prices)):
            count += 1
            if prices[i2] < current:
                break
        answer.append(count)

    return answer
