#!/usr/bin/python3

# помещаем скрипт в директорию cgi-bin
# запускаем сервер python3 -m http.server --cgi
# переданный файл сохраняется рядом со скриптом

import cgi
import os

form = cgi.FieldStorage()

fileitem = form['filename']

name = fileitem.filename
path = '{}/cgi-bin/{}'.format(os.getcwd(), name)
data = fileitem.file.read()

if name:
	with open(path, 'wb') as f:
		f.write(data)
	message = 'Файл {} загружен'.format(name)
else:
	message = 'Файл не загружен'

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Получение файла</title>
        </head>
        <body>""")

print("<p>{}</p>".format(message))

print("""</body>
        </html>""")