def solution(topping):
    answer = 0

    left = {}   # 왼쪽 토핑 개수
    right = {}  # 오른쪽 토핑 개수

    # 처음에는 모든 토핑이 오른쪽에 있음
    for t in topping:
        if t not in right:
            right[t] = 1
        else:
            right[t] += 1

    # 순서대로 잘라보기
    for i in range(len(topping)):
        now = topping[i]

        # 현재 토핑을 왼쪽으로 이동
        if now not in left:
            left[now] = 1
        else:
            left[now] += 1

        # 오른쪽에서는 현재 토핑 하나 제거
        right[now] -= 1

        # 오른쪽에 더 이상 해당 토핑이 없으면 종류에서 제거
        if right[now] == 0:
            del right[now]

        # 왼쪽 토핑 종류 수 == 오른쪽 토핑 종류 수
        if len(left) == len(right):
            answer += 1

    return answer