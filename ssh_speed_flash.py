#!/usr/bin/python3

import paramiko #sudo pip install paramiko
				#sudo pip install cryptography==2.4.2
from timeit import default_timer as timer


host = '192.168.0.1'
user = 'admin'
secret = '1'
port = 22

path = 'tmp/mnt/usb1_1/'
filename = 'myfile'
mbytes = 10

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

res = client.connect(hostname=host, username=user, password=secret, port=port)

t = timer()
stdin, stdout, stderr = client.exec_command('dd if=/dev/zero of=%s%s bs=1M count=%d' % (path, filename, mbytes))

if stderr.read():
    elapsed = timer() - t
    print('Speed = %.2f KBytes/s = %.2f Mbytes/s' % (mbytes * 1024 / elapsed, mbytes / elapsed))

client.close()