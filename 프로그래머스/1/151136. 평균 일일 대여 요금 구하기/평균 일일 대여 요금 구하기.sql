SELECT ROUND(AVG(DAILY_FEE), 0) AS AVERAGE_FEE -- 평균 요금을 반올림해서 출력
FROM CAR_RENTAL_COMPANY_CAR -- 자동차 정보가 있는 테이블
WHERE CAR_TYPE = 'SUV'; -- 자동차 종류가 SUV인 행만 선택