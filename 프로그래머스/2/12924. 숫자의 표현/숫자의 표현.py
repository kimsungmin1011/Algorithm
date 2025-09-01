def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        number=0
        for j in range(i,n+1):
            number+=j
            if number == n:
                answer+=1
            elif number > n:
                break
                
    return answer