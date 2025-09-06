def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len=video_len.split(':')
    video_len=int(video_len[0])*60+int(video_len[1])
    
    pos=pos.split(':')
    pos=int(pos[0])*60+int(pos[1])
    
    op_start=op_start.split(':')
    op_start=int(op_start[0])*60+int(op_start[1])
    
    op_end=op_end.split(':')
    op_end=int(op_end[0])*60+int(op_end[1])
    
    time=pos
    
    if op_start<=time<=op_end:
        time=op_end
    
    for c in commands:
        if c=='next':
            if time+10<=video_len:
                time+=10
            else:
                time=video_len
        else:
            if time-10>=0:
                time-=10
            else:
                time=0
                
        if op_start<=time<=op_end:
            time=op_end
                
    h=str(time//60)
    if len(h)==1:
        h='0'+h
        
    m=str(time%60)
    if len(m)==1:
        m='0'+m
        
    answer = h + ':' + m
    
    return answer