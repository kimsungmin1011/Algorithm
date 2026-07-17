def solution(elements):
    # 원형 수열 처리를 위해 리스트를 2배로 확장
    sums = set()
    n = len(elements)
    
    # 길이 1부터 n까지 반복
    for length in range(1, n + 1):
        # 시작 인덱스
        for i in range(n):
            # 연속된 부분 수열의 합을 구하고 set에 추가
            if i + length < n:
                sub_sum = sum(elements[i : (i + length) % n])
            else:
                sub_sum = sum(elements[i:] + elements[:(i + length) % n])
            sums.add(sub_sum)
            
    return len(sums)
