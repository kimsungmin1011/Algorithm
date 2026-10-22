SELECT P.PRODUCT_CODE, -- 상품코드 출력
       SUM(P.PRICE * O.SALES_AMOUNT) AS SALES -- 상품별 매출 합계
FROM PRODUCT P -- 상품 테이블을 P로 부름
JOIN OFFLINE_SALE O ON P.PRODUCT_ID = O.PRODUCT_ID -- 같은 상품 ID끼리 연결
GROUP BY P.PRODUCT_CODE -- 같은 상품코드끼리 묶음
ORDER BY SALES DESC, P.PRODUCT_CODE ASC; -- 매출 내림차순, 동률이면 상품코드 오름차순