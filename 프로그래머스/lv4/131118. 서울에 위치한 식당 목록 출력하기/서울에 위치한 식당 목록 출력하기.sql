-- 코드를 입력하세요
SELECT RI.REST_ID,REST_NAME,FOOD_TYPE,FAVORITES,ADDRESS,ROUND(AVG(REVIEW_SCORE),2) AS SCORE
FROM REST_INFO RI 
JOIN REST_REVIEW RR ON RI.REST_ID = RR.REST_ID 
WHERE ADDRESS LIKE '서울%'
GROUP BY RI.REST_ID,REST_NAME,FOOD_TYPE,FAVORITES,ADDRESS 
ORDER BY SCORE DESC, FAVORITES DESC;