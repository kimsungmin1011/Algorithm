def calc(arr):
    # 문자열에서 알파벳으로만 이루어진 2글자 조합(bigram)을 추출해 딕셔너리(다중집합)로 반환
    cdict = {}
    for i in range(2, len(arr) + 1):
        # 연속된 두 글자를 추출
        cut_arr = arr[i - 2 : i]

        # 알파벳으로만 구성된 경우가 아니면 무시
        if cut_arr.isalpha() == False:
            continue

        # 처음 나온 bigram이면 1로 초기화
        if cut_arr not in cdict:
            cdict[cut_arr] = 1
        # 이미 존재하면 개수 +1
        else:
            cdict[cut_arr] += 1

    return cdict


def solution(str1, str2):
    answer = 0
    # str1/str2에서 알파벳만으로 된 2글자 조합을 추출해 다중집합 딕셔너리를 만든다
    str1 = str1.lower()
    str2 = str2.lower()

    dict1 = calc(str1)
    dict2 = calc(str2)

    # dict1과 dict2에 존재하는 모든 원소를 포함, 각 원소 개수는 두 딕셔너리에서의 최대값
    final_hap = dict()
    for i in dict1:
        if i in dict2:
            final_hap[i] = max(dict1[i], dict2[i])
        else:
            final_hap[i] = dict1[i]

    for i in dict2:
        if i not in final_hap:
            final_hap[i] = dict2[i]

    # dict1과 dict2에 모두 존재하는 원소만 포함, 각 원소 개수는 두 딕셔너리에서의 최소값
    final_kyo = dict()
    for i in dict1:
        if i in dict2:
            final_kyo[i] = min(dict1[i], dict2[i])

    # 교집합 크기 ÷ 합집합 크기 × 65536, 합집합이 비어있으면 65536 반환
    sum_hap = sum(final_hap.values())
    sum_kyo = sum(final_kyo.values())

    if sum_hap == 0:
        answer = 65536
    else:
        answer = int(sum_kyo / sum_hap * 65536)

    return answer
