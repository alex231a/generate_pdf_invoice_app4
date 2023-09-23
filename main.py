import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("orders/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1", engine='openpyxl')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    f_name = Path(filepath).stem
    order_num = f_name.split('-')[0]
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Order number {order_num}')
    pdf.output(f"PDFs/{f_name}.pdf")
