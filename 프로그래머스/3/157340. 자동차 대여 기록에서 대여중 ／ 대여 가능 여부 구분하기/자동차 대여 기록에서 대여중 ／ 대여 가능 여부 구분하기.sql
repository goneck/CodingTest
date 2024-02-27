select
    his.car_id,
    case when sum(a.cnt) is not null and sum(a.cnt)>0 then '대여중' else '대여 가능' end as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY his
left outer join 
    (select
        car_id,
        count(history_id) as cnt
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    where start_date<='2022-10-16' and end_date>='2022-10-16'
    group by car_id) a
on his.car_id = a.car_id
group by his.car_id
order by car_id desc