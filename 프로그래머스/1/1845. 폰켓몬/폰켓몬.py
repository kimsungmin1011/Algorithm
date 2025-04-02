def solution(nums):
    count = 0
    save = {}

    for i in nums:
        if i not in save:
            save[i] = 1
        else:
            save[i] += 1

    poketmon = set()
    answer = 0

    while count < len(nums) // 2:
        for i in save:
            if count >= len(nums) // 2:
                break

            if save[i] > 0:
                if i not in poketmon:
                    poketmon.add(i)
                    answer += 1
                count += 1
                save[i] -= 1

    return answer
