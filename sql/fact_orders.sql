CREATE TABLE fact_orders
(
    sales_document BIGINT,
    item_number INT,
    customer_id VARCHAR(20),

    material_number VARCHAR(50),

    quantity INT,

    net_price DECIMAL(10,2),

    order_value DECIMAL(12,2),

    order_date DATE,

    order_status VARCHAR(30),

    PRIMARY KEY (sales_document,item_number)
);
