select product_id, product_name, product_cd, category, price -- 식품 정보 출력
from food_product -- 식품 정보 테이블
where price = (
    select max(price) from food_product -- 가장 높은 가격 구하기
); -- 가격이 최고 가격과 같은 식품만 선택