#!/usr/bin/python3

import smtplib, getpass, os
from configparser import ConfigParser


def send_email(emails, subject, text):

    config_path = os.path.abspath('email.ini')

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print('Config not found! Exiting!')
        sys.exit(1)

    host = cfg.get('smtp', 'server')
    from_addr = cfg.get('smtp', 'from_addr')

    body = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (from_addr, emails, subject, text)

    password = getpass.getpass()

    server = smtplib.SMTP_SSL(host)
    server.login('mrqiwi@ya.ru',password)
    server.sendmail(from_addr, emails, body)
    server.quit()

if __name__ == "__main__":

    emails = ['drqiwi@gmail.com', '7ssa7@inbox.ru']
    subject = 'check connection'
    text = 'hi, my friend'

    print(emails)
    send_email(emails, subject, text)