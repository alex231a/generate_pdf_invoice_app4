import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("./*.txt")
pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:
    pdf.add_page()
    f_name = Path(filepath).stem
    title = f_name.title()
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'{title}')
pdf.output(f"output.pdf")
