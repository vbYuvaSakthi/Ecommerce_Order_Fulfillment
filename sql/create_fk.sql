ALTER TABLE fact_orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id)
REFERENCES dim_customers(customer_id);

ALTER TABLE fact_deliveries
ADD CONSTRAINT fk_deliveries_customer
FOREIGN KEY (customer_id)
REFERENCES dim_customers(customer_id);

ALTER TABLE fact_shipments
ADD CONSTRAINT fk_shipments_customer
FOREIGN KEY (customer_id)
REFERENCES dim_customers(customer_id);