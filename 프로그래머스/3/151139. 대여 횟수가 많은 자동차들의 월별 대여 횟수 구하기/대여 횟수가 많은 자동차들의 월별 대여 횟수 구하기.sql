-- 코드를 입력하세요
/* SELECT MONTH(CH.START_DATE) AS MONTH, CH.CAR_ID, COUNT(CAR_ID) AS RECORDS FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY CH WHERE MONTH(CH.START_DATE) BETWEEN 8 AND 10 GROUP BY MONTH, CH.CAR_ID HAVING COUNT(CAR_ID)!=0
ORDER BY MONTH, CAR_ID DESC
*/
SELECT MONTH(CH.START_DATE) AS MONTH, CH.CAR_ID, COUNT(CH.CAR_ID) AS RECORDS 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY CH 
INNER JOIN (SELECT CAR_ID, COUNT(CAR_ID) AS CNT FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY CH
            WHERE MONTH(CH.START_DATE) BETWEEN 8 AND 10 GROUP BY CAR_ID HAVING CNT>=5) CH2 
            ON CH.CAR_ID = CH2.CAR_ID
WHERE CH2.CNT>4
GROUP BY CH.CAR_ID, MONTH(CH.START_DATE) 
HAVING MONTH BETWEEN 8 AND 10 AND RECORDS!=0 
ORDER BY MONTH, CH.CAR_ID DESC