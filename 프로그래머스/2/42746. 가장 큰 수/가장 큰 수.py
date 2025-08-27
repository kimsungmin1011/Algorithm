def solution(numbers):
    numbers=[str(i) for i in numbers]
    numbers.sort(key=lambda i: i * 5, reverse=True)
    return str(int("".join(numbers)))