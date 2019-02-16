#!/usr/bin/env python3

import os
import xlwt
from datetime import datetime

dirname = 'output'
filename = 'my_file.xls'
sheetname = 'A Test Sheet'

font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 5
font0.bold = True

style0 = xlwt.XFStyle()
style0.font = font0

style1 = xlwt.XFStyle()
style1.num_format_str = 'D-MMM-YY'

wb = xlwt.Workbook()
ws = wb.add_sheet(sheetname)

ws.write(0, 0, 'Test')
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))


if not os.path.exists(dirname):
	os.mkdir(dirname)

os.chdir(dirname)

wb.save(filename)
