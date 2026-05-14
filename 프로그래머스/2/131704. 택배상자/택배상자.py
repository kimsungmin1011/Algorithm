from collections import deque


def solution(order):
    answer = 0
    main = deque([i + 1 for i in range(len(order))])
    sub = deque([])

    current = 0
    while current < len(order):
        if main and order[current] == main[0]:
            main.popleft()
            current += 1
        elif sub and order[current] == sub[-1]:
            sub.pop()
            current += 1
        elif main:
            sub.append(main.popleft())
        else:
            break

    return current
