#!/usr/bin/python3
#TODO сделать проще
import requests
import getpass
import smtplib
import re
from sys import argv
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_rate():

    page = requests.get('https://www.finanz.ru/valyuty/v-realnom-vremeni-rub')

    soup = BeautifulSoup(page.text, 'lxml')

    table = soup.findChildren('table')

    my_table = table[1]

    rows = my_table.findChildren(['th', 'tr'])

    line = ""
    lines = []

    for row in rows:
        cells = row.findChildren('td')

        for cell in cells:
            line += cell.text + " "

        if line or line.strip():
            if "USD/" in line or "EUR/" in line:
                lines.append(line)

        line = ""

    return "%s\n%s" % (lines[0], lines[1])

def send_email(data, email_to, password):

    re_email=re.compile(r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}")

    if not re_email.findall(email_to):
        print("неверный email %s" % (email_to))
        return None

    email_from = "mrqiwi@ya.ru"

    msg = MIMEMultipart()
    msg["Subject"] = "курс валют"
    msg["From"] = email_from
    msg["To"] = email_to
    msg.attach(MIMEText(data, "plain"))

    server = smtplib.SMTP_SSL("smtp.yandex.ru")

    try:
        server.login(email_from, password)
        server.send_message(msg)
        print("Письмо успешно отправлено!(%s)" % email_to)
    except smtplib.SMTPException as err:
        print("Ошибка при отправке письма:", err)
    finally:
        server.quit()


if __name__ == "__main__":

    if len(argv) < 2:
        print("укажить email")
        exit(1)

    rate = get_rate()

    password = getpass.getpass("пароль-> ")

    i = 1
    while i < len(argv):
        send_email(rate, argv[i], password)
        i += 1

    exit(0)


