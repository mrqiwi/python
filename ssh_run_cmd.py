#!/usr/bin/python3

import paramiko #sudo pip install paramiko
				#sudo pip install cryptography==2.4.2

host = '192.168.0.1'
user = 'admin'
secret = 'admin'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

res = client.connect(hostname=host, username=user, password=secret, port=port)

stdin, stdout, stderr = client.exec_command('sbin/ifconfig')

data = stdout.read()

if data:
	#декодируем полученные байты в строку для наглядности
	str_data = data.decode()
	print(str_data)
else:
	print('\nstderr: ', stderr.read())

client.close()
