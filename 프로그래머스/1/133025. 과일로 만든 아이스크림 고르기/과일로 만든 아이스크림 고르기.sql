SELECT F.FLAVOR -- 아이스크림 맛 출력
FROM FIRST_HALF F -- 상반기 주문 정보 테이블을 F로 부름
JOIN ICECREAM_INFO I ON F.FLAVOR = I.FLAVOR -- 같은 맛끼리 성분 정보 연결
WHERE F.TOTAL_ORDER > 3000 -- 총주문량이 3000 초과
AND I.INGREDIENT_TYPE = 'fruit_based' -- 주성분이 과일인 것
ORDER BY F.TOTAL_ORDER DESC; -- 총주문량이 많은 순서로 정렬