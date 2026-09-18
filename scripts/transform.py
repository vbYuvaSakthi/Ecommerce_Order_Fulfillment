import pandas as pd
file_path = "data/SAP-DataSet.xlsx"
kna1 = pd.read_excel(file_path,sheet_name="KNA1")
lfa1 = pd.read_excel(file_path,sheet_name="LFA1")
vbak = pd.read_excel(file_path,sheet_name="VBAK")
vbap = pd.read_excel(file_path,sheet_name="VBAP")
likp = pd.read_excel(file_path,sheet_name="LIKP")
lips = pd.read_excel(file_path,sheet_name="LIPS")
vttk = pd.read_excel(file_path,sheet_name="VTTK")
vttp = pd.read_excel(file_path,sheet_name="VTTP")

#Remove Duplicates
kna1 = kna1.drop_duplicates()
lfa1 = lfa1.drop_duplicates()
vbak = vbak.drop_duplicates()
vbap = vbap.drop_duplicates()
likp = likp.drop_duplicates()
lips = lips.drop_duplicates()
vttk = vttk.drop_duplicates()
vttp = vttp.drop_duplicates()

#Remove Extra Spaces
dataframes = [
    kna1,lfa1,vbak,vbap,
    likp,lips,vttk,vttp
]
for df in dataframes:
    df.columns = df.columns.str.strip()
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].astype(str).str.strip()

#Filling Null Values
for df in dataframes:
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("Unknown")

#Convert Dates
vbak["Order Date"] = pd.to_datetime(
    vbak["Order Date"]
)
vbap["Delivery Date"] = pd.to_datetime(
    vbap["Delivery Date"]
)
likp["Delivery Date"] = pd.to_datetime(
    likp["Delivery Date"]
)
vttk["Shipment Date"] = pd.to_datetime(
    vttk["Shipment Date"]
)
vttp["Shipment Date"] = pd.to_datetime(
    vttp["Shipment Date"]
)

#Create Order Value
vbap["Order Value"] = (
    vbap["Quantity"]
    * vbap["Net Price"]
)

#Create Delivery Analytics Dataset
delivery_analytics = pd.merge(
    vbak,
    likp,
    on=["Sales Document","Customer ID"],
    how="inner"
)
delivery_analytics[
    "Processing_Days"
] = (
    delivery_analytics["Delivery Date"]
    -
    delivery_analytics["Order Date"]
).dt.days

#Create Delivery Performance Flag
delivery_analytics[
    "Delivery_Performance"
] = delivery_analytics[
    "Processing_Days"
].apply(
    lambda x:
    "On Time"
    if x <= 7
    else "Delayed"
)

## =====================================================
# RENAME COLUMNS - DIM_CUSTOMERS
# =====================================================

dim_customers = kna1.rename(columns={
    "Customer ID": "customer_id",
    "Customer Name": "customer_name",
    "Country": "country",
    "Region": "region",
    "City": "city",
    "Postal Code": "postal_code",
    "Street Address": "street_address",
    "Phone Number": "phone_number",
    "Email Address": "email_address",
    "Language": "language",
    "Customer Group": "customer_group"
})

dim_customers = dim_customers[
    [
        "customer_id",
        "customer_name",
        "country",
        "region",
        "city",
        "postal_code",
        "street_address",
        "phone_number",
        "email_address",
        "language",
        "customer_group"
    ]
]

# =====================================================
# RENAME COLUMNS - DIM_CARRIERS
# =====================================================

dim_carriers = lfa1.rename(columns={
    "Vendor Number": "vendor_number",
    "Vendor Name": "vendor_name",
    "Country": "country",
    "City": "city",
    "Payment Terms": "payment_terms"
})

dim_carriers = dim_carriers[
    [
        "vendor_number",
        "vendor_name",
        "country",
        "city",
        "payment_terms"
    ]
]

# =====================================================
# FACT_ORDERS (VBAK + VBAP)
# =====================================================

fact_orders = pd.merge(
    vbak,
    vbap,
    on="Sales Document",
    how="inner"
)

fact_orders["order_value"] = (
    fact_orders["Quantity"] *
    fact_orders["Net Price"]
)

fact_orders = fact_orders.rename(columns={
    "Sales Document": "sales_document",
    "Item Number": "item_number",
    "Customer ID": "customer_id",
    "Material Number": "material_number",
    "Quantity": "quantity",
    "Net Price": "net_price",
    "Order Date": "order_date",
    "Order Status": "order_status"
})

fact_orders = fact_orders[
    [
        "sales_document",
        "item_number",
        "customer_id",
        "material_number",
        "quantity",
        "net_price",
        "order_value",
        "order_date",
        "order_status"
    ]
]

# =====================================================
# FACT_DELIVERIES
# =====================================================

fact_deliveries = likp.rename(columns={
    "Delivery Number": "delivery_number",
    "Sales Document": "sales_document",
    "Customer ID": "customer_id",
    "Delivery Date": "delivery_date",
    "Shipping Type": "shipping_type",
    "Delivery Status": "delivery_status"
})

fact_deliveries = fact_deliveries[
    [
        "delivery_number",
        "sales_document",
        "customer_id",
        "delivery_date",
        "shipping_type",
        "delivery_status"
    ]
]

# =====================================================
# FACT_SHIPMENTS
# =====================================================

fact_shipments = vttk.rename(columns={
    "Shipment Number": "shipment_number",
    "Delivery Number": "delivery_number",
    "Customer ID": "customer_id",
    "Carrier": "carrier",
    "Shipment Date": "shipment_date",
    "Shipment Status": "shipment_status"
})

fact_shipments = fact_shipments[
    [
        "shipment_number",
        "delivery_number",
        "customer_id",
        "carrier",
        "shipment_date",
        "shipment_status"
    ]
]

# =====================================================
# CHECK OUTPUT COLUMN NAMES
# =====================================================

print("\nDIM_CUSTOMERS")
print(dim_customers.columns.tolist())

print("\nDIM_CARRIERS")
print(dim_carriers.columns.tolist())

print("\nFACT_ORDERS")
print(fact_orders.columns.tolist())

print("\nFACT_DELIVERIES")
print(fact_deliveries.columns.tolist())

print("\nFACT_SHIPMENTS")
print(fact_shipments.columns.tolist())

#CSV files
dim_customers.to_csv(
    "output/dim_customers.csv",
    index=False
)

dim_carriers.to_csv(
    "output/dim_carriers.csv",
    index=False
)

fact_orders.to_csv(
    "output/fact_orders.csv",
    index=False
)

fact_deliveries.to_csv(
    "output/fact_deliveries.csv",
    index=False
)

fact_shipments.to_csv(
    "output/fact_shipments.csv",
    index=False
)

delivery_analytics.to_csv(
    "output/delivery_analytics.csv",
    index=False
)

print("All MySQL Ready CSV Files Generated Successfully")

with open("output/dim_customers.csv", "r") as f:
    print(f.readline())