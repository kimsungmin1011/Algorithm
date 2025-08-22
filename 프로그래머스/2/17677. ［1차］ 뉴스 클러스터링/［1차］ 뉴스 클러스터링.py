def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    answer = 0
    hapdict = {}
    hapdict2 = {}
    kyodict = {}
    kyodict2 = {}

    for i in range(2, len(str1) + 1):
        arr = "".join([i for i in str1[i - 2 : i] if i.isalpha()])
        if len(arr) != 2:
            continue
        if arr not in hapdict:
            hapdict[arr] = 1
        else:
            hapdict[arr] += 1

    for i in range(2, len(str2) + 1):
        arr = "".join([i for i in str2[i - 2 : i] if i.isalpha()])
        if len(arr) != 2:
            continue
        if arr not in hapdict2:
            hapdict2[arr] = 1
        else:
            hapdict2[arr] += 1

    final_hap = dict()
    for i in hapdict:
        if i in hapdict2:
            final_hap[i] = max(hapdict[i], hapdict2[i])
        else:
            final_hap[i] = hapdict[i]

    for i in hapdict2:
        if i not in final_hap:
            final_hap[i] = hapdict2[i]

    for i in range(2, len(str1) + 1):
        arr = "".join([i for i in str1[i - 2 : i] if i.isalpha()])
        if len(arr) != 2:
            continue
        if arr not in kyodict:
            kyodict[arr] = 1
        else:
            kyodict[arr] += 1

    for i in range(2, len(str2) + 1):
        arr = "".join([i for i in str2[i - 2 : i] if i.isalpha()])
        if len(arr) != 2:
            continue
        if arr not in kyodict2:
            kyodict2[arr] = 1
        else:
            kyodict2[arr] += 1

    final_kyo = dict()
    for i in kyodict:
        if i in kyodict2:
            final_kyo[i] = min(kyodict[i], kyodict2[i])

    if sum(final_kyo.values()) != 0 and sum(final_hap.values()) != 0:
        answer = sum(final_kyo.values()) / sum(final_hap.values()) * 65536 // 1
    elif sum(final_kyo.values()) == 0 and sum(final_hap.values()) == 0:
        answer = 65536
    else:
        answer = 0
    # print(str1, str2)
    # print(final_hap, final_kyo)
    return answer
