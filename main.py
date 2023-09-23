import pandas as pd
import glob

filepaths = glob.glob("orders/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1", engine='openpyxl')
    print(df)