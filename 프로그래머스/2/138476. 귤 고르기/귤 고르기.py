def solution(k, tangerine):
    answer = 0
    number = [0 for i in range(max(tangerine) + 1)]

    for i in tangerine:
        number[i] += 1
    
    number.sort(reverse=True)
    
    for i in number:
        if k > 0:
            k-=i
            answer+=1
        else:
            break
    
    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
