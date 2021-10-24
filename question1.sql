'''
Prepared by: Renjith Paul
Prepared on: 17-01-2021
Purpose : This SQL program is to run the go-jek SQL analysis query.
Assumption: 
    a)No date filters applied.
    b)Used IANA timezone notation.
'''

select 
    order_date,
    LENGTH(order_type) - LENGTH(REGEXP_REPLACE(order_type, ',', '')) + 1 no_of_services,
    sum(count(customer_no)) over (partition by  order_date,LENGTH(order_type) - LENGTH(REGEXP_REPLACE(order_type, ',', '')) + 1 ) total_customer,
    order_type,
    count(customer_no) as total_customer_per_order_type,
    order_payment
from (
    select 
        customer_no,
        STRING_AGG(distinct order_type ORDER BY order_type) AS order_type,
        STRING_AGG(distinct order_payment ORDER BY order_payment) AS order_payment,
        EXTRACT(DATE FROM DATETIME(order_time, "Asia/Jakarta")) order_date 
    from `bi-dwhdev-01.source.daily_order`
    where  order_status='Completed'
    group by customer_no,order_date
    )
group by order_date,order_type,order_payment
order by order_date,no_of_services,order_type,order_payment;