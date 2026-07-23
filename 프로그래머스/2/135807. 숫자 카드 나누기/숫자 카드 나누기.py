def solution(arrayA, arrayB):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def get_gcd(numbers):
        result = numbers[0]

        for number in numbers[1:]:
            result = gcd(result, number)

        return result

    def is_valid(candidate, other_array):
        # 상대방의 모든 카드가 candidate로 나누어지지 않아야 함
        return all(number % candidate != 0 for number in other_array)

    gcd_a = get_gcd(arrayA)
    gcd_b = get_gcd(arrayB)

    answer_a = gcd_a if is_valid(gcd_a, arrayB) else 0
    answer_b = gcd_b if is_valid(gcd_b, arrayA) else 0

    return max(answer_a, answer_b)