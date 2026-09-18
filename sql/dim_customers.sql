USE ecommerce_dw;

CREATE TABLE dim_customers
(
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100),
    country VARCHAR(50),
    region VARCHAR(50),
    city VARCHAR(50),
    postal_code VARCHAR(20),
    street_address VARCHAR(255),
    phone_number VARCHAR(50),
    email_address VARCHAR(100),
    language VARCHAR(20),
    customer_group VARCHAR(20)
);