def solution(s):
    result = []
    # 설명: 문자열 길이가 1이면 압축 불필요 → 1 반환
    if len(s) == 1:
        return 1

    # 설명: i는 압축 단위 (1부터 문자열 길이의 절반까지)
    for i in range(1, len(s) // 2 + 1):
        re = 0  # 설명: 압축된 문자열 '길이'를 누적
        cnt = 1  # 설명: 같은 문자열이 반복된 횟수
        tmp = s[:i]  # 설명: 현재 비교할 문자열 단위 초기값 (처음 i글자)

        # 설명: j는 i 간격으로 진행. len(s)+i까지 보는 이유는
        #      마지막 블록을 '강제로' 처리(else 진입)하기 위함
        for j in range(i, len(s) + i, i):
            # 설명: 현재 tmp와 다음 i글자가 같으면 반복 수 증가
            if tmp == s[j : j + i]:
                cnt += 1
            else:
                # 설명: 반복이 끝났으니, 지금까지의 블록을 결과 길이에 반영
                if cnt != 1:
                    # 숫자(반복 횟수)의 자릿수 + 블록 길이
                    re += len(str(cnt)) + len(tmp)
                else:
                    # 반복 1회면 숫자 없이 블록 길이만
                    re += len(tmp)
                # 다음 블록으로 갱신
                tmp = s[j : j + i]
                cnt = 1

        result.append(re)

    # 설명: 압축 단위를 1..n//2로 시도한 길이들과, 원문 길이 중 최소 반환
    return min(min(result), len(s))
