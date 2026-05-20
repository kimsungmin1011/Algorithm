def solution(number, k):
    stack = []  # 결과를 만들어갈 스택

    for num in number:
        # 스택 top보다 현재 숫자가 더 크면, top을 버린다 (k번까지)
        # → 앞자리를 더 큰 수로 만들수록 전체 수가 커지기 때문
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # 끝까지 다 돌았는데도 제거할 횟수(k)가 남아있다면
    # → 남은 숫자들이 내림차순/같음 상태라는 뜻이므로 뒤에서부터 잘라낸다
    # 예: "54321", k=2 → "543"
    if k > 0:
        stack = stack[:-k]

    return "".join(stack)