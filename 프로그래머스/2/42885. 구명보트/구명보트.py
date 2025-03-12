def solution(people, limit):
    people.sort()
    boat = 0
    i = 0
    j = len(people) - 1
    
    while i <= j:
        # 가벼운 사람 + 무거운 사람 한 보트에 태울 수 있는지 체크
        if people[i] + people[j] <= limit:
            i += 1
        # 실패하면 무거운 사람만 우선 보트에 태움
        j -= 1
        boat += 1
    
    return boat