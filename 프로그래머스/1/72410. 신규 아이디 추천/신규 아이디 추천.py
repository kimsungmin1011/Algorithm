def solution(new_id):
    # 신규 아이디 추천을 위한 알고리즘 구현
    answer = ""
    new_list = []

    # 1단계: new_id의 모든 문자를 순회하며 소문자로 변환하고, 허용된 문자만 필터링하여 new_list에 추가
    for i in new_id:
        if 65 <= ord(i) <= 90:
            i = chr(ord(i) + 32)
            new_list.append(i)
        elif (
            97 <= ord(i) <= 122
            or i == "-"
            or i == "_"
            or i == "."
            or 48 <= ord(i) <= 57
        ):
            new_list.append(i)

    new_id = new_list[:]
    new_list = [new_id[0]]

    # 2단계: 연속된 '.'를 하나로 치환하여 new_list에 추가
    for i in range(1, len(new_id)):
        if new_id[i] == "." and new_id[i - 1] == ".":
            continue
        else:
            new_list.append(new_id[i])

    new_id = new_list[:]
    new_list = []

    # 3단계: 시작과 끝에 위치한 '.'을 제거
    for i in range(len(new_id)):
        if (i == 0 or i == len(new_id) - 1) and new_id[i] == ".":
            continue
        else:
            new_list.append(new_id[i])

    new_id = new_list[:]
    new_list = []

    # 4단계: new_id가 빈 문자열인 경우 'a'를 추가
    if len(new_id) == 0:
        new_id.append("a")

    # 5단계: new_id의 첫 15개 문자만 남기기
    new_id = new_id[:15]

    # 만약 제거 후 끝에 마침표가 있다면 제거한다
    if new_id[-1] == ".":
        new_id.pop()

    # 6단계: 아이디 길이가 3 미만일 경우 마지막 문자를 반복하여 길이를 3으로 맞추기
    while len(new_id) < 3:
        new_id.append(new_id[-1])

    answer = "".join(new_id)
    return answer
