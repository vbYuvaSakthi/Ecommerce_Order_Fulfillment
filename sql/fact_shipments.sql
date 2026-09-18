CREATE TABLE fact_shipments
(
    shipment_number BIGINT PRIMARY KEY,
    delivery_number BIGINT,
    customer_id VARCHAR(20),
    carrier VARCHAR(50),
    shipment_date DATE,
    shipment_status VARCHAR(30)
);