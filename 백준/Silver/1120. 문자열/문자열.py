a, b = input().split()  # 문자열 A, B 입력 받음
min_diff = 51  # 차이 최댓값보다 큰 수로 초기화 (최대 A길이 = 50)

# B 위에 A를 덮을 수 있는 모든 위치에서 비교해봄
for start in range(len(b) - len(a) + 1):
    diff = 0  # 이 위치에서 A랑 B가 다른 글자 수

    # A를 한 글자씩 B랑 비교
    for j in range(len(a)):
        if a[j] != b[start + j]:  # 글자가 다르면
            diff += 1  # 차이 +1

    min_diff = min(min_diff, diff)  # 최소 차이 저장

print(min_diff)  # 정답 출력
