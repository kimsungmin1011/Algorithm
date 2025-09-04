def solution(numbers):
    stack = []                     # '뒤에 큰 수'를 아직 못 찾은 인덱스 저장
    answer = [-1] * len(numbers)   # 기본값 -1로 초기화

    for i in range(len(numbers)):
        # 현재 수가 스택 맨 위 인덱스의 값보다 크면,
        # 그 인덱스의 '뒤 큰 수'는 바로 현재 값
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        # 현재 인덱스는 아직 뒤 큰 수를 못 찾았으므로 스택에 대기
        stack.append(i)

    return answer