#!/usr/bin/python3

import telnetlib

host = '192.168.0.1'
user = 'admin'
password = 'admin'

tn = telnetlib.Telnet(host)

tn.read_until(b'login: ')
tn.write(user.encode('ascii') + b'\n')

tn.read_until(b'Password: ')
tn.write(password.encode('ascii') + b'\n')

tn.write(b'ls\n')
tn.write(b'exit\n')
print(tn.read_all().decode())