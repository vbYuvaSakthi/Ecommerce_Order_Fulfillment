SELECT
AVG(processing_days) AS avg_processing_time
FROM vw_delivery_analytics;

SELECT
ROUND(
    SUM(
        CASE
            WHEN delivery_performance = 'On Time'
            THEN 1
            ELSE 0
        END
    ) * 100 / COUNT(*),
2) AS on_time_delivery_rate
FROM vw_delivery_analytics;

SELECT
AVG(processing_days) AS average_delivery_time
FROM vw_delivery_analytics;

SELECT
carrier,
COUNT(*) AS total_shipments,
AVG(processing_days) AS avg_delivery_days
FROM vw_delivery_analytics
GROUP BY carrier
ORDER BY avg_delivery_days;

SELECT
ROUND(
    SUM(
        CASE
            WHEN delivery_status = 'Delivered'
            THEN 1
            ELSE 0
        END
    ) * 100 / COUNT(*),
2
) AS fulfillment_efficiency
FROM vw_delivery_analytics;

SELECT
delivery_status,
COUNT(*) AS total_orders
FROM vw_delivery_analytics
GROUP BY delivery_status;

