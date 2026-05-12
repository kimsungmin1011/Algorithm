def solution(genres, plays):
    answer = []

    # 장르별 노래 정보를 저장할 딕셔너리
    # key: 장르, value: [(재생 수, 고유 번호), ...]
    song = {}

    # 장르별 총 재생 수를 저장할 딕셔너리
    # key: 장르, value: 해당 장르의 총 재생 수
    song_total = {}

    # 모든 노래를 순회하면서 장르별로 묶고, 총 재생 수를 계산
    for i in range(len(genres)):
        if genres[i] not in song:
            # 처음 나온 장르라면 새로 등록
            song[genres[i]] = [(plays[i], i)]
            song_total[genres[i]] = plays[i]
        else:
            # 이미 있는 장르라면 노래 정보 추가
            song[genres[i]].append((plays[i], i))
            song_total[genres[i]] += plays[i]

    # 장르 목록 생성
    key_list = [i for i in song]

    # 장르별 총 재생 수가 많은 순서대로 정렬
    key_list.sort(key=lambda x: -song_total[x])

    # 총 재생 수가 많은 장르부터 순회
    for i in key_list:
        # 장르 내부에서 재생 수 내림차순, 고유 번호 오름차순으로 정렬
        song[i].sort(key=lambda x: (-x[0], x[1]))

        # 해당 장르에서 1등 노래의 고유 번호 추가
        answer.append(song[i][0][1])

        # 해당 장르에서 2등 노래의 고유 번호 추가
        if len(song[i]) > 1:
            answer.append(song[i][1][1])

    return answer