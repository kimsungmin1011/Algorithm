from collections import deque
import math

n = int(input())


# 소수 판별 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


for _ in range(n):
    first, last = input().split()

    # BFS를 사용하여 최소 변경 횟수를 구함
    queue = deque([(first, 0)])
    visited = [False] * 10000  # 4자리 숫자 범위
    visited[int(first)] = True

    def bfs():
        while queue:
            number, count = queue.popleft()

            if number == last:  # 목표 숫자에 도달한 경우
                return count

            # 숫자를 한 자리씩 변경
            for i in range(4):
                for digit in range(10):
                    if digit != int(number[i]):  # 같은 숫자로 바꾸지 않기
                        new_number = list(number)
                        new_number[i] = str(digit)
                        real_number = int("".join(new_number))

                        # 숫자가 1000 이상이고, 소수이며, 방문하지 않은 경우
                        if (
                            real_number >= 1000
                            and is_prime(real_number)
                            and not visited[real_number]
                        ):
                            visited[real_number] = True
                            queue.append(("".join(new_number), count + 1))

        return "Impossible"

    print(bfs())
