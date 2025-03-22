def solution(arr):
    answer = []

    for i in range(len(arr)):
        if len(answer) > 0 and arr[i] == answer[-1]:
            continue
        else:
            answer.append(arr[i])

    return answer
