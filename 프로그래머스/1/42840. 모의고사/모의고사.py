def solution(answers):
    answer = []
    n = len(answers)

    count1, count2, count3 = 0, 0, 0

    array1 = [1, 2, 3, 4, 5]
    array2 = [2, 1, 2, 3, 2, 4, 2, 5]
    array3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(n):
        if answers[i] == array1[i % len(array1)]:
            count1 += 1
        if answers[i] == array2[i % len(array2)]:
            count2 += 1
        if answers[i] == array3[i % len(array3)]:
            count3 += 1

    max_answer = max(count1, count2, count3)

    if count1 == max_answer:
        answer.append(1)
    if count2 == max_answer:
        answer.append(2)
    if count3 == max_answer:
        answer.append(3)

    return answer
