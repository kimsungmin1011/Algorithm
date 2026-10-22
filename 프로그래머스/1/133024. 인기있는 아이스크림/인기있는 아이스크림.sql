SELECT FLAVOR -- 아이스크림 맛 출력
FROM FIRST_HALF -- 상반기 주문 정보 테이블
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC; -- 총주문량 내림차순, 동률이면 출하 번호 오름차순