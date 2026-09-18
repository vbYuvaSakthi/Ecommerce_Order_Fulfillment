USE ecommerce_dw;

CREATE TABLE dim_carriers
(
    vendor_number BIGINT PRIMARY KEY,
    vendor_name VARCHAR(100),
    country VARCHAR(50),
    city VARCHAR(50),
    payment_terms VARCHAR(50)
);