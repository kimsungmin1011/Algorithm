from collections import defaultdict


def binary_search(scores, target):
    """
    점수 리스트에서 target 이상이 처음 등장하는 위치(인덱스)를 반환
    """
    left, right = 0, len(scores)
    answer = right  # 기본값: scores 전체 길이 (조건을 만족하는 인덱스가 없을 경우)
    if right == 0:
        return 0
    while left < right:
        mid = (left + right) // 2
        if scores[mid] >= target:
            answer = mid
            right = mid
        else:
            left = mid + 1
    return answer


def solution(infoes, queries):
    # 지원자 정보를 조합별로 저장할 딕셔너리 생성
    applicants = defaultdict(list)

    # 1) infoes 순회하며 16가지 (lang/job/career/food or '-') 조합에 점수 저장
    for info in infoes:
        lang, job, career, food, score = info.split()
        score = int(score)
        for l in (lang, "-"):
            for j in (job, "-"):
                for c in (career, "-"):
                    for f in (food, "-"):
                        key = l + j + c + f
                        applicants[key].append(score)

    # 2) 각 조합별 점수 리스트 오름차순 정렬
    for key in applicants:
        applicants[key].sort()

    answer = []
    # 3) queries 순회하며
    for q in queries:
        # "and " 제거 → ['lang','job','career','food','score']
        parts = q.replace("and ", "").split()
        target = int(parts[-1])  # 기준 점수
        key = "".join(parts[:-1])  # 검색 키

        # 4) 이진 탐색으로 조건을 만족하는 지원자 수 계산
        idx = binary_search(applicants[key], target)
        count = len(applicants[key]) - idx
        answer.append(count)

    return answer
