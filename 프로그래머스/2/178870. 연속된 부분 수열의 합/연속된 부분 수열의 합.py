def solution(sequence, k):
    left, right = 0, 0
    total = sequence[0]
    answer = []

    while left <= right <= len(sequence) - 1:
        if total == k:
            answer.append([left, right])
            total -= sequence[left]
            left += 1
            right += 1
            if right <= len(sequence) - 1:
                total += sequence[right]

        elif total > k:
            total -= sequence[left]
            left += 1

        else:
            right += 1
            if right <= len(sequence) - 1:
                total += sequence[right]

    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]
