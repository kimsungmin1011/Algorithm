def solution(msg):
    # LZW 압축 알고리즘 최적화 버전: 해시 맵(dict) 사용
    answer = []
    # 사전 초기화: A-Z 알파벳 (문자열 → 인덱스)
    word_dict = {chr(ord("A") + i): i + 1 for i in range(26)}
    next_idx = 27  # 다음에 추가될 사전 인덱스
    idx = 0
    n = len(msg)

    # 메시지 전체를 한 번에 훑으며 압축
    while idx < n:
        w = msg[idx]       # 현재까지 매칭된 문자열
        j = idx + 1
        # 가능한 한 긴 문자열을 찾는다
        while j < n and (w + msg[j]) in word_dict:
            w += msg[j]
            j += 1

        # 매칭된 w의 사전 인덱스 추가
        answer.append(word_dict[w])

        # 새롭게 발견된 문자열(w + 다음 문자)을 사전에 등록
        if j < n:
            word_dict[w + msg[j]] = next_idx
            next_idx += 1

        # 다음 탐색 시작 위치 갱신
        idx = j

    return answer