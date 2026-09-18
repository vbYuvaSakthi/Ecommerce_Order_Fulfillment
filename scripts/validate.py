import pandas as pd

file_path = "data/SAP-DataSet.xlsx"

sheets = pd.read_excel(
    file_path,
    sheet_name=None,
    engine="openpyxl"
)

print("\nDATA VALIDATION REPORT\n")

for sheet_name, df in sheets.items():

    print(f"\n----- {sheet_name} -----")

    print("Missing Values")
    print(df.isnull().sum())

    print("\nDuplicate Records")
    print(df.duplicated().sum())

#Customer Referential Integrity
kna1 = sheets["KNA1"]
vbak = sheets["VBAK"]
invalid_customers = vbak[
    ~vbak["Customer ID"].isin(
        kna1["Customer ID"]
    )
]
print("\nINVALID CUSTOMER RECORDS")
print(invalid_customers.shape[0])

#Delivery Referential Integrity
likp = sheets["LIKP"]
vttk = sheets["VTTK"]
invalid_delivery = vttk[
    ~vttk["Delivery Number"].isin(
        likp["Delivery Number"]
    )
]
print("\nINVALID DELIVERY RECORDS")
print(invalid_delivery.shape[0])

#Quantity check
vbap = sheets["VBAP"]
negative_qty = vbap[
    vbap["Quantity"] <= 0
]
print("\nNEGATIVE QUANTITY RECORDS")
print(negative_qty.shape[0])

#Price check
negative_price = vbap[
    vbap["Net Price"] <= 0
]
print("\nNEGATIVE PRICE RECORDS")
print(negative_price.shape[0])

