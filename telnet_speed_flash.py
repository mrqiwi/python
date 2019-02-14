#!/usr/bin/python3

import telnetlib
from timeit import default_timer as timer

host = '192.168.0.1'
user = 'admin'
password = 'admin'

path = 'tmp/mnt/usb1_1/'
filename = 'myfile'
mbytes = 10
cmd = 'dd if=/dev/zero of=%s%s bs=1M count=%d\n' % (path, filename, mbytes)

tn = telnetlib.Telnet(host)

tn.read_until(b'login: ')
tn.write(user.encode('ascii') + b'\n')

tn.read_until(b'Password: ')
tn.write(password.encode('ascii') + b'\n')

print('file = %d mbytes\n' % (mbytes))

print('start...')
t = timer()
tn.write(cmd.encode('ascii'))
tn.read_until(b'records out')
elapsed = timer() - t
print('finish!!')

tn.write(b'exit\n')
tn.read_all().decode()

print('Speed = %.2f KBytes/s = %.2f Mbytes/s' % (mbytes * 1024 / elapsed, mbytes / elapsed))


