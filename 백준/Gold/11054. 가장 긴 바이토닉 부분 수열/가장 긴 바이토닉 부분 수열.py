n = int(input())
arr = list(map(int, input().split()))

# 1) inc[i] = arr[0..i] 중에서 arr[i]를 끝으로 하는 가장 긴 증가 부분수열 길이
inc = [1] * n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            inc[i] = max(inc[i], inc[j] + 1)

# 2) dec[i] = arr[i..n-1] 중에서 arr[i]를 시작으로 하는 가장 긴 감소 부분수열 길이
dec = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if arr[j] < arr[i]:
            dec[i] = max(dec[i], dec[j] + 1)

# 3) i를 꼭대기로 했을 때 바이토닉 부분수열의 최대 길이 계산
answer = 0
for i in range(n):
    answer = max(answer, inc[i] + dec[i] - 1)

print(answer)
