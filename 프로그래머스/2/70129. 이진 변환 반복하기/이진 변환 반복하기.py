change,count=0,0

def solution(s):
    global change,count
    
    # 0 제거하는 함수
    def del0(number):
        global count
        new=[]
        
        for n in number:
            if n=='0':
                count+=1
                continue
            new.append(n)
        
        return new
    
    # 문자열 길이를 2진수로 변환
    def leejin(number):
        answer=[]
        l=len(number)
        flag=False # 첫 1이 나오기 전까지 0이 들어가면 안됨
        i=17 # 2**17 = 13만이므로 여기가 최대임
        # 2의 거듭제곱의 차수를 1씩 줄여가며 탐색
        while i>=0:
            if l>=2**i:
                answer.append('1')
                l-=2**i
                flag=True
            elif flag==True:
                answer.append('0')
            i-=1
            
        return answer
    
    s=list(s)
    while True:
        if len(s)==1 and s[0]=='1':
            return [change,count]
        
        # 0없애기
        s=del0(s)
        # 문자열 길이 2진수로 변환
        s=leejin(s)
        
        change+=1 # 이진변환 횟수 + 1
        
        
                