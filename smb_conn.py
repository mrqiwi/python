#!/usr/bin/python3

import tempfile
import smb
import shutil

from smb.SMBConnection import SMBConnection

user_name   = '1'
password    = '1'
ip_server   = '192.168.0.1'
local_machine_name  = 'pc'
server_machine_name = 'D-LINK'
share_name  = 'share'
file_name   = 'ubuntu-16.04.4-server-amd64.iso'

# create and establish connection
conn = SMBConnection(user_name, password, local_machine_name, server_machine_name, use_ntlm_v2 = True)

assert conn.connect(ip_server, 139)

# print list of files at the root of the share
files = conn.listPath(share_name, '/')
for item in files:
    print(item.filename)

# check if the file we want is there
sf = conn.getAttributes(share_name, 'ny.jpg')
print('size = ', sf.file_size)
print('name = ', sf.filename)

# create a temporary file for the transfer
file_obj = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
file_name = file_obj.name
file_attributes, copysize = conn.retrieveFile(share_name, "rti_license.dat", file_obj)
print(copysize)
file_obj.close()

# # copy temporary file
shutil.copy(file_name, "rti_license.dat")

# close connection
conn.close()