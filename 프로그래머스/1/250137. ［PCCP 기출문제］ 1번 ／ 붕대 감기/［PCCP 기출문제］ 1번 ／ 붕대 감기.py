def solution(bandage, health, attacks):
    btime,shp,php=bandage[0], bandage[1], bandage[2]
    ctime, chp = 0, health
    
    for i in range(len(attacks)):
        atime,ahp=attacks[i][0], attacks[i][1]
        chp+=(atime-ctime)*shp + (atime-ctime)//btime*php
        if chp>health:
            chp=health
        ctime=atime+1
        chp-=ahp
        if chp<=0:
            return -1
    
    return chp