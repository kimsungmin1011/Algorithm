def solution(n):
    answer = 0
    n = list(str(n))
    n = sorted(n, reverse = True) 
    answer = int("".join(n))
    return answer