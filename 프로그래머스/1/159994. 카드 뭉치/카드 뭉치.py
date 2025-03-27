from collections import deque


def solution(cards1, cards2, goal):
    answer = ""
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    save = []

    for i in goal:
        if cards1 and i == cards1[0]:
            save.append(cards1.popleft())
        elif cards2 and i == cards2[0]:
            save.append(cards2.popleft())

    if save == goal:
        answer = "Yes"
    else:
        answer = "No"

    return answer
