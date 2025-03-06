s = list(input())  # 문자열을 리스트로 변환하여 문자 하나씩 접근

count0 = 0  # 연속된 '0' 블록 개수
count1 = 0  # 연속된 '1' 블록 개수
flag1 = False  # '1' 블록이 현재 활성화된 상태인지 여부
flag0 = False  # '0' 블록이 현재 활성화된 상태인지 여부

for i in s:
    if int(i) == 1:  # 현재 문자가 '1'일 경우
        if flag0 == True:  # 이전에 '0' 블록이 있었다면 종료
            flag0 = False

        if flag1 == False:  # 새로운 '1' 블록이 시작됨
            flag1 = True
            count1 += 1  # '1' 블록 개수 증가

    else:  # 현재 문자가 '0'일 경우
        if flag1 == True:  # 이전에 '1' 블록이 있었다면 종료
            flag1 = False

        if flag0 == False:  # 새로운 '0' 블록이 시작됨
            flag0 = True
            count0 += 1  # '0' 블록 개수 증가

# 최소 뒤집기 연산 출력 (둘 중 더 적은 값 선택)
print(min(count0, count1))
