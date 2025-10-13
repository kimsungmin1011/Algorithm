N = int(input())     # 찾고자 하는 'IOI' 패턴의 반복 횟수 (예: N=2면 'IOIOI' 찾기)
M = int(input())     # 문자열 S의 길이
S = input()          # 입력 문자열
answer, i, count = 0, 0, 0  # 결과(패턴 개수), 현재 인덱스, 현재까지 연속된 'IOI' 개수

# 문자열 전체를 순회
while i < (M - 1):  # 인덱스 범위를 벗어나지 않도록 M-1까지만
    # 현재 위치에서 3글자('IOI') 패턴이 있는지 확인
    if S[i:i+3] == 'IOI':
        i += 2          # 'IOI'는 3글자지만, 겹치는 부분이 있으므로 2칸만 이동
        count += 1      # 연속된 'IOI' 발견 → 카운트 증가

        # count가 N(필요한 연속 개수)와 같으면, 패턴 1개 완성
        if count == N:
            answer += 1     # 패턴 하나 발견
            count -= 1      # 다음 겹치는 패턴 고려 위해 1 감소 (ex. 'IOIOI' → 다음 'IOI')
    else:
        i += 1          # 'IOI' 패턴이 아니면 다음 인덱스로
        count = 0       # 연속 카운트 초기화

print(answer)