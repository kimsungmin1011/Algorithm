def solution(s):
    s1 = s.lstrip("{").rstrip("}").split("},{")
    sets = [list(map(int, x.split(","))) for x in s1]
    sets.sort(key=len)

    answer = []
    seen = set()

    for group in sets:
        for num in group:
            if num not in seen:
                seen.add(num)
                answer.append(num)

    return answer