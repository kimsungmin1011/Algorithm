SELECT -- 결과에 보여줄 항목 선택
    U.USER_ID, -- 사용자 ID
    U.NICKNAME, -- 사용자 닉네임
    SUM(B.PRICE) AS TOTAL_SALES -- 사용자별 거래금액 합계
FROM USED_GOODS_BOARD B -- 거래 게시글 테이블을 B로 부름
JOIN USED_GOODS_USER U ON B.WRITER_ID = U.USER_ID -- 작성자 ID로 사용자 정보 연결
WHERE B.STATUS = 'DONE' -- 거래가 완료된 게시글만 선택
GROUP BY U.USER_ID -- 같은 사용자끼리 묶기
HAVING SUM(B.PRICE) >= 700000 -- 합계가 70만 원 이상인 사용자만 선택
ORDER BY TOTAL_SALES ASC; -- 총거래금액이 적은 순서로 정렬