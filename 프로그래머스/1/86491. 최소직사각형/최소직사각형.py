def solution(sizes):
    answer = 0
    long_length = []
    short_length = []

    for size in sizes:
        long_length.append(max(size))
        short_length.append(min(size))

    answer = max(long_length) * max(short_length)

    return answer
