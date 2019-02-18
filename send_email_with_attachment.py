#!/usr/bin/python3

import smtplib, getpass, os
from configparser import ConfigParser
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate


def send_email(emails, subject, text, file_to_attach):

    # get the config
    config_path = os.path.abspath('email.ini')

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print('Config not found! Exiting!')
        sys.exit(1)

    host = cfg.get('smtp', 'server')
    from_addr = cfg.get('smtp', 'from_addr')

    # create the message
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['Subject'] = subject
    msg['Date'] = formatdate(localtime=True)

    if text:
        msg.attach(MIMEText(text))

    msg['To'] = ', '.join(emails)

    attachment = MIMEBase('application', 'octet-stream')
    header = 'Content-Disposition', 'attachment; filename="%s"' % file_to_attach

    try:
        with open(file_to_attach, 'rb') as fh:
            data = fh.read()

        attachment.set_payload(data)
        encoders.encode_base64(attachment)
        attachment.add_header(*header)
        msg.attach(attachment)
    except IOError:
        msg = 'Error opening attachment file %s' % file_to_attach
        print(msg)
        sys.exit(1)

    password = getpass.getpass()

    server = smtplib.SMTP_SSL(host)
    server.login('mrqiwi@ya.ru',password)
    server.sendmail(from_addr, emails, msg.as_string())
    server.quit()

if __name__ == "__main__":

    emails = ['drqiwi@gmail.com', '7ssa7@inbox.ru']
    subject = 'check connection'
    text = 'hi, my friend'
    path = 'venok.jpg'

    send_email(emails, subject, text, path)




