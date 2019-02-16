#!/usr/bin/env python3

import os
from fpdf import FPDF

dirname = 'output'

def change_fonts():    
    filename = 'simple_demo.pdf'
    font_size = 8

    pdf = FPDF()
    pdf.add_page()

    for font in pdf.core_fonts:
        if any([letter for letter in font if letter.isupper()]):
            # пропускаем данный шрифт.
            continue
        pdf.set_font(font, size=font_size)
        txt = "Font name: {} - {} pts".format(font, font_size)
        pdf.cell(0, 10, txt=txt, ln=1, align="C")
        font_size += 2
 
    pdf.output(filename)
 
def draw_lines():    
    filename = 'draw_lines.pdf'

    pdf = FPDF()
    pdf.add_page()
    pdf.line(10, 10, 10, 100)
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)
    pdf.line(20, 20, 100, 20)

    pdf.output(filename)    
 

if __name__ == '__main__':

    if not os.path.exists(dirname):
        os.mkdir(dirname)
    os.chdir(dirname)

    change_fonts()
    draw_lines()


