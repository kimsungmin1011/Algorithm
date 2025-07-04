n = int(input())
liquid = list(map(int, input().split()))

# 투 포인터
left = 0
right = n - 1

result_value = int(1e10)  # 절댓값 비교를 위한 초기값
answer_x, answer_y = 0, 0  # 최종 두 용액 저장 변수

while left < right:
    value = liquid[left] + liquid[right]  # 현재 두 용액의 합

    # 최소 절댓값 갱신
    if abs(value) < abs(result_value):
        result_value = value
        answer_x, answer_y = liquid[left], liquid[right]

    # 합이 0보다 작으면 왼쪽 포인터 이동
    if value < 0:
        left += 1
    # 합이 0보다 크면 오른쪽 포인터 이동
    elif value > 0:
        right -= 1
    # 합이 정확히 0이라면 정답이므로 종료
    else:
        break

print(answer_x, answer_y)
