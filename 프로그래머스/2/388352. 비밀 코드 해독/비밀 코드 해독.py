def solution(n, q, ans):
    answer = 0
    number_list=[]
    arr=[]
    
    # 1 ~ n까지 숫자 중 5개를 조합 선택하는 백트래킹 함수
    def dfs(idx):
        if len(arr)==5:
            number_list.append(arr[:])
            return
        
        for i in range(idx,n+1):
            arr.append(i)
            dfs(i+1)
            arr.pop()
    
    dfs(1)
    
    for number in number_list:
        # 현재 정수 조합을 모든 입력 정수와 비교
        flag = True
        for m in range(len(q)):
            count=0
            # 입력 정수의 각 숫자가 현재 정수 조합에 있는지 탐색
            for i in q[m]:
                if i in number:
                    count+=1
            # 시스템 응답과 일치하지 않는다면
            if count!=ans[m]:
                flag=False
                break
        # 현재 정수 조합이 모든 시도의 응답을 통과했다면
        if flag==True:
            answer+=1
            
    return answer