from collections import deque


def solution(progresses, speeds):
    answer = []
    # p_queue = deque(progresses)

    while len(progresses) != 0:
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while True:
            if len(progresses) > 0 and progresses[0] >= 100:
                # p_queue.popleft()
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                break

        if count > 0:
            answer.append(count)

    return answer
