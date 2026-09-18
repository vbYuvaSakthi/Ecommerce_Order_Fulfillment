SELECT
    o.sales_document,
    c.customer_name,
    o.order_date
FROM fact_orders o
JOIN dim_customers c
ON o.customer_id = c.customer_id
LIMIT 10;