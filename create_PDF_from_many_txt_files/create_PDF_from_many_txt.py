import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("./*.txt")
pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()
    pdf.add_page()
    f_name = Path(filepath).stem
    title = f_name.title()
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'{title}', ln=1)

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output(f"output.pdf")
