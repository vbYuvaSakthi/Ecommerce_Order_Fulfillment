SELECT
order_status,
COUNT(*) AS total_orders
FROM fact_orders
GROUP BY order_status;

SELECT
delivery_status,
COUNT(*) AS total_deliveries
FROM fact_deliveries
GROUP BY delivery_status;

SELECT
customer_id,
SUM(order_value) AS total_revenue
FROM fact_orders
GROUP BY customer_id
ORDER BY total_revenue DESC;