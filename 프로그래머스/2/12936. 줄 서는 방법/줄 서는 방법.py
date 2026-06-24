import math

def solution(n, k):
    answer = []
    # 1부터 n까지의 사람 번호 리스트 (파이썬 인덱스는 0부터 시작)
    people = [i for i in range(1, n + 1)]
    k -= 1  # 0번째 인덱스 기준으로 맞추기 위해 k에서 1을 뺌
    
    while n > 0:
        # (n-1)!의 값을 구함
        fact = math.factorial(n - 1)
        
        # 현재 자릿수에서 들어갈 사람의 인덱스
        idx = k // fact
        
        # answer에 해당 사람을 추가하고, people 리스트에서 제거
        answer.append(people.pop(idx))
        
        # 다음 단계의 k값으로 업데이트
        k %= fact
        n -= 1
        
    return answer
