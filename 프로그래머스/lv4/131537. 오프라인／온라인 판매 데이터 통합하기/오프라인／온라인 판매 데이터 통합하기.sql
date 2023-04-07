-- 코드를 입력하세요
SELECT *
FROM 
(SELECT SUBSTRING(a.SALES_DATE, 1,10) as SALES_DATE, a.PRODUCT_ID, a.USER_ID, a.SALES_AMOUNT
FROM ONLINE_SALE a
UNION
SELECT SUBSTRING(b.SALES_DATE, 1,10) as SALES_DATE, b.PRODUCT_ID, NULL as USER_ID, b.SALES_AMOUNT
FROM OFFLINE_SALE b) c 
WHERE c.SALES_DATE like '2022-03%'
ORDER BY 1, 2, 3