#!/usr/bin/python3

import imaplib
import getpass
import email
from clint.textui import progress


mail = imaplib.IMAP4_SSL('imap.yandex.ru')

login = 'mrqiwi@ya.ru'
password = getpass.getpass()
match = ['notification@facebookmail.com',
		 'promotion@aliexpress.com',
		 'transaction@notice.aliexpress.com',
		 'message@notice.aliexpress.com',
		 'buy@aliexpress.com',
		 'transaction_seller@notice.aliexpress.com',
		 'alisourcepro@service.alibaba.com']

mail.login(login, password)

status, select_data = mail.select('INBOX')

#получаем количество входящих писем
nmessages = int(select_data[0].decode('utf-8'))

lcounter = 0
#пробегаемся по входящим письмам
for n in progress.bar(range(1, nmessages)):

	status, msg_data = mail.fetch(b'%d' % (n), '(RFC822)')

	msg = email.message_from_bytes(msg_data[0][1])

	try:
		trash, from_addr = email.utils.parseaddr(msg['From'])

	except Exception as e:
		#если не можем прочитать From то пропускаем письмо
		if str(e) == "object of type 'Header' has no len()":
			continue
		else:
			print('letter#%d: %s' % (n, e))
			break

	if from_addr in match:
		lcounter += 1
		#помечаем письмо
		mail.store(b'%d' % (n), '+FLAGS', '\\Deleted')

#удаляем помеченные письма
mail.expunge()
print('%d писем удалено' % (lcounter))

mail.logout()