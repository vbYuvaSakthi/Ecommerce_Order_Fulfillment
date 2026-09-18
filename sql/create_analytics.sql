DROP VIEW vw_delivery_analytics;
CREATE VIEW vw_delivery_analytics AS
SELECT
    o.sales_document,
    o.customer_id,
    o.order_date,

    d.delivery_date,
    d.delivery_status,

    s.carrier,
    s.shipment_status,

    DATEDIFF(
        d.delivery_date,
        o.order_date
    ) AS processing_days,

    CASE
        WHEN DATEDIFF(
            d.delivery_date,
            o.order_date
        ) <= 7
        THEN 'On Time'
        ELSE 'Delayed'
    END AS delivery_performance

FROM fact_orders o

JOIN fact_deliveries d
    ON o.sales_document = d.sales_document

JOIN fact_shipments s
    ON d.delivery_number = s.delivery_number;