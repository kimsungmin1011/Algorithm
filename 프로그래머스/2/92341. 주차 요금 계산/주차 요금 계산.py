import math


def solution(fees, records):
    records = [i.split(" ") for i in records]
    answer = []
    car = {}
    park = {}

    for time, number, flag in records:
        time = time.split(":")
        time = int(time[0]) * 60 + int(time[1])
        if number not in car:
            car[number] = 0

        if number not in park:
            park[number] = time
        else:
            car[number] += time - park[number]
            park.pop(number)

    for number in park:
        car[number] += 1439 - park[number]

    car_number = [i for i in car.keys()]
    car_number.sort(key=lambda x: int(x))

    for number in car_number:
        if car[number] <= fees[0]:
            answer.append(fees[1])
        else:
            cost = fees[1] + math.ceil((car[number] - fees[0]) / fees[2]) * fees[3]
            answer.append(cost)

    return answer
