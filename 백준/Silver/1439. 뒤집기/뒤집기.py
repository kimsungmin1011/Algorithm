dasom = input()  # 문자열을 그대로 사용
go = 0
back = 0

if dasom[0] == '0':
    go += 1
else:
    back += 1
    
# 첫 번째 문자부터 마지막 문자까지 확인
for i in range(len(dasom) - 1):
    if dasom[i + 1] == '0' and dasom[i] != dasom[i + 1]:
        go += 1
    elif dasom[i + 1] == '1' and dasom[i] != dasom[i + 1]:
        back += 1

# 결과 출력 부분 수정
print(min(go, back))
