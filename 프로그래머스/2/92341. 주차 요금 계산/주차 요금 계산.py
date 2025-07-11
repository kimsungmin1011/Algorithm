import math  # 올림 계산을 위해 math.ceil 사용


def solution(fees, records):
    # fees: [기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)]
    # records: ["HH:MM 차량번호 IN/OUT", ...] 형태의 리스트

    # 1) 문자열 파싱: ["HH:MM", "차량번호", "IN"/"OUT"]
    records = [i.split(" ") for i in records]
    answer = []  # 최종 요금 리스트
    car = {}  # 차량별 누적 주차 시간(분)
    park = {}  # 차량별 마지막 입차 시간(분)

    # 2) 입차/출차 기록 처리
    for time, number, flag in records:
        # "HH:MM" -> 분 단위 정수로 변환
        time = time.split(":")
        time = int(time[0]) * 60 + int(time[1])

        # 처음 본 차량이면 누적 시간 0으로 초기화
        if number not in car:
            car[number] = 0

        # 입차 처리
        if number not in park:
            park[number] = time
        # 출차 처리
        else:
            # (출차 시각 - 입차 시각)을 누적 주차 시간에 더함
            car[number] += time - park[number]
            # 입차 기록 제거
            park.pop(number)

    # 3) 출차 기록 없는 차량은 23:59에 출차한 것으로 간주
    for number in park:
        # 23*60+59 = 1439분
        car[number] += 1439 - park[number]

    # 4) 차량 번호 오름차순 정렬 (문자열이지만 숫자 기준으로)
    car_number = [i for i in car.keys()]
    car_number.sort(key=lambda x: int(x))

    # 5) 요금 계산
    for number in car_number:
        # 누적 주차 시간
        t = car[number]
        # 기본시간 이하라면 기본요금만
        if t <= fees[0]:
            answer.append(fees[1])
        else:
            # 초과 시간에 대해 단위시간으로 나누고 올림한 뒤 단위요금 곱하기
            extra = math.ceil((t - fees[0]) / fees[2])
            cost = fees[1] + extra * fees[3]
            answer.append(cost)

    return answer
