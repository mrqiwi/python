#!/usr/bin/python3

import imaplib
import getpass
import email
# from pprint import pprint


mail = imaplib.IMAP4_SSL('imap.mail.ru')

login = '7ssa7@inbox.ru'
password = getpass.getpass()

mail.login(login, password)

#список доступных каталогов
# pprint(mail.list())

mail.select('INBOX')

status, inlist = mail.search(None, 'ALL')
#список номеров писем
# print(inlist)

#получаем письмо по номеру в необработанном виде
status, msg_data = mail.fetch(b'20', '(RFC822)')

msg = email.message_from_bytes(msg_data[0][1])

trash, to_addr = email.utils.parseaddr(msg['To'])
trash, from_addr = email.utils.parseaddr(msg['From'])
letter = msg.get_payload()

print('Date: ' + msg['Date'])
print('Subject: ' + msg['Subject'])
print('To: ' + to_addr)
print('From: ' + from_addr)
print('Letter:\n' + letter)

mail.logout()