#!/usr/bin/python3

#TODO добавить возможность выбора даты
from selenium import webdriver
from bs4 import BeautifulSoup
from sys import argv
import xlwt

def get_timetable(station1 = "Рязань-1", station2 = "Перевлес"):
#---------------------------excel-----------------------------#
    filename = '%s->%s.xls' % (station1, station2)
    sheetname = 'Timetable'

    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 5
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0

    wb = xlwt.Workbook()
    ws = wb.add_sheet(sheetname)
	#колонку маршрута и режима делаем чуть шире
    ws.col(3).width = 4200
    ws.col(4).width = 5000

    ws.write(0, 0, "Отпр.")
    ws.write(0, 1, "Приб.")
    ws.write(0, 2, "В пути")
    ws.write(0, 3, "Режим движения")
    ws.write(0, 4, "Маршрут движения")
    ws.write(0, 5, "Цена")

	#----------------------webdriver------------------------------#
    chromedriver = '/usr/local/bin/chromedriver'
    options = webdriver.ChromeOptions()
	#браузер не видно
    options.add_argument('headless')
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

    browser.get('https://www.tutu.ru/prigorod/')

    st1 = browser.find_element_by_name("st1")
    st2 = browser.find_element_by_name("st2")
    btn = browser.find_element_by_class_name("inner_wrapper")

    st1.clear()
    st1.send_keys(station1)

    st2.clear()
    st2.send_keys(station2)

    btn.click()

	#---------------------BeautifulSoup----------------------------#
    requiredHtml = browser.page_source

    soup = BeautifulSoup(requiredHtml, 'html5lib')
    table = soup.findChildren('table')
    my_table = table[0]

    rows = my_table.findChildren(['th', 'tr'])

    nrow = 1
    for row in rows:
        cells = row.findChildren('td')
        #если cells летит пустым то возвращаем предыдущее значение nrow
	    #чтобы таблица не опускалась вниз
        if not cells:
            nrow -=1
        ncol = 0
        for cell in cells:
            value = cell.text
            ws.write(nrow, ncol, value)
            ncol += 1
        nrow += 1

    wb.save(filename)
    browser.close()
    print("файл '%s' создан" % (filename))

if __name__ == '__main__':

    if len(argv) == 3:
        get_timetable(argv[1], argv[2])
    else:
        get_timetable()



