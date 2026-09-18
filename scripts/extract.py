import pandas as pd
file_path = "data/SAP-DataSet.xlsx"
sheets = pd.read_excel(
    file_path,
    sheet_name=None,
    engine="openpyxl"
)
print("\nSAP Sheets Loaded Successfully\n")
for sheet_name, df in sheets.items():
    print(f"Sheet : {sheet_name}")
    print(f"Rows  : {df.shape[0]}")
    print(f"Cols  : {df.shape[1]}")
    print("-" * 50)


    