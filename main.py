import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("orders/*.xlsx")

for filepath in filepaths:
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

    # print(df)
    df = pd.read_excel(filepath, sheet_name="Sheet 1", engine='openpyxl')
    title_list = list(df.columns)
    title_list = [item.replace("_", " ").capitalize() for item in title_list]

    pdf.set_font(family='Times', size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=str(title_list[0]), border=1)
    pdf.cell(w=70, h=8, txt=str(title_list[1]), border=1)
    pdf.cell(w=35, h=8, txt=str(title_list[2]), border=1)
    pdf.cell(w=30, h=8, txt=str(title_list[3]), border=1)
    pdf.cell(w=30, h=8, txt=str(title_list[4]), border=1, ln=1)

    for index, row in df.iterrows():
        if str(row["product_id"]) != 'nan':
            pdf.set_font(family='Times', size=10)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
            pdf.cell(w=70, h=8, txt=str(row['product_name']), border=1)
            pdf.cell(w=35, h=8, txt=str(row['amount_purchased']), border=1)
            pdf.cell(w=30, h=8, txt=str(row['amount_purchased']), border=1)
            pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)

    total_price = df['total_price'].sum()
    pdf.set_font(family='Times', size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=" ", border=1)
    pdf.cell(w=70, h=8, txt=" ", border=1)
    pdf.cell(w=35, h=8, txt=" ", border=1)
    pdf.cell(w=30, h=8, txt=" ", border=1)
    pdf.cell(w=30, h=8, txt=str(total_price), border=1, ln=1)

    pdf.set_font(family='Times', size=14, style='B')
    pdf.cell(w=30, h=8, txt=f"The total price is {total_price}.",  ln=1)

    pdf.set_font(family='Times', size=14, style='B')
    pdf.cell(w=30, h=8, txt="Python How")
    pdf.image("pythonhow.png", w=10)


    pdf.output(f"PDFs/{f_name}.pdf")
