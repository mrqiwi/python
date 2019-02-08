#!/usr/bin/python3

import urllib.request
from smb.SMBHandler import SMBHandler
import io

user_name   = '1'
password    = '1'
ip_server   = '192.168.0.1'
share_name  = 'share'
file_name   = 'ubuntu-16.04.4-server-amd64.iso'

buf = io.StringIO()
buf.write("smb://%s:%s@%s/%s/%s" % (user_name, password, ip_server, share_name, file_name))

file_fh = open(file_name, 'rb')

director = urllib.request.build_opener(SMBHandler)
fh = director.open(buf.getvalue(), data = file_fh)


fh.close()