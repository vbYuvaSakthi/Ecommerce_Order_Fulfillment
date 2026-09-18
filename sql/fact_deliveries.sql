CREATE TABLE fact_deliveries
(
    delivery_number BIGINT PRIMARY KEY,
    sales_document BIGINT,
    customer_id VARCHAR(20),
    delivery_date DATE,
    shipping_type VARCHAR(30),
    delivery_status VARCHAR(30)
);