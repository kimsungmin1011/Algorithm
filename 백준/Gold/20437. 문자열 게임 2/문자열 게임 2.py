from collections import defaultdict
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    word = input()  # 문자열 (보통 마지막에 '\n'이 포함될 수 있음)
    k = int(input())  # 어떤 문자가 정확히 k번 포함되는 부분문자열을 찾는다

    # dic[ch] = ch가 등장한 인덱스들을 저장하는 리스트
    dic = defaultdict(list)

    # min_len / max_len은 "인덱스 차이" 기준으로 관리 (실제 길이는 +1)
    min_len = 1e9
    max_len = -1

    # 1) 문자별로 등장 위치(인덱스) 수집
    # 예: word="abac" -> dic['a']=[0,2], dic['b']=[1], dic['c']=[3]
    for i in range(len(word)):
        dic[word[i]].append(i)

    # 2) 각 문자에 대해, 등장 위치 리스트에서 "연속 k개"를 잡아 구간 길이 계산
    # arr = [p0, p1, p2, ...] 일 때
    # arr[i] ~ arr[i+k-1] 구간은 해당 문자가 정확히 k번 포함되는 부분문자열 후보
    for key in dic.keys():
        arr = dic[key]

        # 해당 문자가 k번 이상 등장해야 후보 구간이 존재
        if len(arr) >= k:
            # 연속 k개 묶음을 모두 확인
            for i in range(len(arr) - k + 1):
                # 양 끝 인덱스 차이 (예: 2~4면 4-2=2)
                length = arr[i + k - 1] - arr[i]

                # 최소/최대 갱신 (아직 +1 안 한 상태)
                min_len = min(min_len, length)
                max_len = max(max_len, length)

    # 3) 후보가 하나도 없으면 -1
    if min_len == 1e9:
        print(-1)
    else:
        # 인덱스 차이 -> 실제 문자열 길이로 바꾸기 위해 +1
        # 예: 인덱스 2~4는 글자 수 3이므로 (4-2)+1
        print(min_len + 1, max_len + 1)
