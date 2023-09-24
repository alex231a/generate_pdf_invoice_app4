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
    f_name_list = f_name.split('-')
    order_num = f_name_list[0]
    f_date = f_name_list[1]

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Order number {order_num}', ln=1)

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Date {f_date}', ln=1)

    pdf.output(f"PDFs/{f_name}.pdf")
