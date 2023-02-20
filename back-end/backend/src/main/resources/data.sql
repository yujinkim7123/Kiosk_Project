-- category 데이터 추가
INSERT INTO table_category(category_name) VALUES("hamburger");
INSERT INTO table_category(category_name) VALUES("beverage");
INSERT INTO table_category(category_name) VALUES("sidemenu");
INSERT INTO table_category(category_name) VALUES("vegetable");
INSERT INTO table_category(category_name) VALUES("pattie");
INSERT INTO table_category(category_name) VALUES("bread");
INSERT INTO table_category(category_name) VALUES("etc");


-- ingredient 데이터 추가
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("먹물번_윗면", 500, 6) ;
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("머핀번_윗면", 300, 6) ;
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("기본번_윗면", 400, 6) ;
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("돼지고기", 500, 5) ;
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("소고기", 700, 5) ;
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("계란", 600, 5) ;
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("버섯", 200, 4) ;
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("상추", 300, 4) ;
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("토마토", 250, 4) ;
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("오이", 250, 4) ;
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("양파", 250, 4) ;
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("치즈", 400, 7) ;
INSERT INTO table_ingredient(ingredient_name, ingredient_price, category_id) VALUES("햄", 500, 7) ;

-- menu 데이터 추가
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("초코 쉐이크", 4000, 2) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("우유", 2000, 2) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("오렌지 주스", 3500, 2) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("스프라이트", 2000, 2) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("환타", 2000, 2) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("딸기쉐이크", 3500, 2) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("코카콜라", 2000, 2) ;

INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("해쉬브라운", 1500, 3) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("프렌치 프라이", 1500, 3) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("바닐라 선데이 아이스크림", 1500, 3) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("상하이치킨스낵랩", 2500, 3) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("초코 선데이 아이스크림", 1500, 3) ;

INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("빅맥", 3500, 1) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("치즈버거", 3500, 1) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("불고기버거", 3500, 1) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("더블치즈", 3500, 1) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("쿼터파운더 치즈", 3500, 1) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("베이컨 토마토 디럭스", 3500, 1) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("에그 불고기버거", 3500, 1) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("불고기버거 세트", 3500, 1) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("치즈버거 세트", 3500, 1) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("더블치즈버거 세트", 3500, 1) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("쿼터파운더 치즈버거 세트", 3500, 1) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("베이컨 토마토 디럭스 세트", 3500, 1) ;
INSERT INTO table_menu(menu_name, menu_price, category_id) VALUES("에크 불고기버거 세트", 3500, 1) ;

-- 저장 과정
-- user 데이터 추가
-- INSERT INTO table_user(user_name, is_easy, kiosk_height) VALUES("사람1", 1, 2);
-- INSERT INTO table_user(user_name, is_easy, kiosk_height) VALUES("사람2", 0, 3);

-- 한 명의 유저와 선택한 옵션 여러개
-- 선택한 하나 이상의 메뉴가 넘어옴

-- 주문이 들어오면 USER와 메뉴를 이용하여 ORDER를 먼저 생성
-- ORDER 데이터 추가
-- INSERT INTO table_order(total_count, total_price, is_packaging, order_date, user_id) VALUES(1, 3000, false,"1999-12-31", 1);
-- INSERT INTO table_order(total_count, total_price, is_packaging, order_date, user_id) VALUES(3, 8500, true,"1999-01-01", 2);
-- INGREDIENT와 Menu로 ORDER_DETAIL 생성
-- INSERT INTO table_order_detail(menu_count, each_menu_price, is_set, order_id, menu_id) VALUES(1, 3000, false, 1, 1);
-- INSERT INTO table_order_detail(menu_count, each_menu_price, is_set, order_id, menu_id) VALUES(2, 3000, false, 2, 2);
-- INSERT INTO table_order_detail(menu_count, each_menu_price, is_set, order_id, menu_id) VALUES(1, 2500, true, 2, 2);
-- MenuDetail로 Custom 생성 가능

-- 결제 시에 받을 데이터
-- 유저 정보
-- 전체 주문 생성 (메뉴 정보, 카테고리 정보)
-- 커스텀 정보 생성 (재료정보, 카테고리 정보)
-- 상세 주문 생성 (주문, 커스텀, 메뉴, 정보들 사용)

