from collections import deque


def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    answer = 0

    while queue:
        current = queue.popleft()

        # 중요도가 더 높은 프로세스가 뒤에 있다면, 현재 프로세스를 뒤로 보냄
        if queue and max(q[1] for q in queue) > current[1]:
            queue.append(current)
        else:
            answer += 1
            if current[0] == location:
                return answer
