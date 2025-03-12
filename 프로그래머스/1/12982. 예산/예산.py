def solution(d, budget):
    # 0/1 배낭문제 스타일의 문제
    answer = 0
    d.sort()
    
    for i in d:
        if budget >= i:
            budget -= i
            answer += 1
        else:
            break
            
    return answer