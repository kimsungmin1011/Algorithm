# Python 풀이
s = input()
c4 = input()
c4arr = [i for i in c4]

temp = []
for idx in range(len(s)):
    temp.append(s[idx])
    if temp[-1] == c4arr[-1]:  # 둘이 뒷글자가 같다면?
        # 게다가 길이도 최소 c4arr의 길이보다 같거나 그 이상일 경우>
        if len(c4arr) <= len(temp):
            # 검증들어가자.
            if temp[-len(c4arr) :] == c4arr:
                for i in range(len(c4arr)):
                    temp.pop()
if temp:
    print("".join(map(str, temp)))
else:
    print("FRULA")
