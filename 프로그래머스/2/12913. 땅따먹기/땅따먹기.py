def solution(land):         
    for i in range(1,len(land)):
        for j in range(4):
            cm=0
            for k in range(4):
                if j!=k:
                    cm=max(cm,land[i-1][k])
            land[i][j]+=cm
            
    return max(land[-1])