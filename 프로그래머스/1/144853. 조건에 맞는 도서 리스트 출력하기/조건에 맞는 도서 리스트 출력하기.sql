SELECT BOOK_ID, -- 도서 ID 출력
       PUBLISHED_DATE AS PUBLISHED_DATE -- 출판일을 년-월-일로 출력
FROM BOOK -- 도서 정보 테이블
WHERE YEAR(PUBLISHED_DATE) = 2021 -- 출판 연도가 2021년
  AND CATEGORY = '인문' -- 카테고리가 인문인 도서
ORDER BY PUBLISHED_DATE ASC; -- 출판일이 빠른 순서로 정렬