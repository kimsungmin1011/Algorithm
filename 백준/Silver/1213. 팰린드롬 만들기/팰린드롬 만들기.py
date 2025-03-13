def make_palindrome(s):
    # 1. 문자의 개수를 세기 위한 딕셔너리 생성
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # 2. 홀수 개수의 문자들을 저장할 리스트 생성
    odd_chars = []
    for char, count in char_count.items():
        if count % 2 == 1:
            odd_chars.append(char)

    # 3. 홀수 개수의 문자가 1개 이상이면 팰린드롬을 만들 수 없다
    if len(odd_chars) > 1:
        return "I'm Sorry Hansoo"

    # 4. 팰린드롬의 앞부분을 생성한다
    palindrome_front = ''
    for char, count in sorted(char_count.items()):
        palindrome_front += char * (count // 2)
    
    # 5. 팰린드롬의 중간부분 (홀수 개수의 문자가 있다면)
    palindrome_middle = ''
    if odd_chars:
        palindrome_middle = odd_chars[0]
    
    # 6. 팰린드롬의 뒷부분은 앞부분의 역순이다
    palindrome_back = palindrome_front[::-1]
    
    # 7. 완성된 팰린드롬을 반환한다
    return palindrome_front + palindrome_middle + palindrome_back

# 입력
s = input().strip()
# 출력
print(make_palindrome(s))
