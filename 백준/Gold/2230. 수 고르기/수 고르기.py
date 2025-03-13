N,M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()

left,right = 0,1
result = 2e9

while left <= right < N:
    diff = nums[right]-nums[left]

    if diff == M:
        result = M
        break
    elif diff < M:
        right += 1
    else:
        result = min(result, diff)
        left += 1

print(result)