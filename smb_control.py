#!/usr/bin/python3

# -*- coding: utf-8 -*-
# Attention: Please use pysmb 1.1.14

from io import StringIO
from smb import smb_structs
from nmb.NetBIOS import NetBIOS
import os, shutil
from tempfile import NamedTemporaryFile as NTF
from smb.SMBConnection import SMBConnection
from smb.SMBHandler import SMBHandler
from timeit import default_timer as timer



def getBIOSName(remote_smb_ip, timeout=5):
  try:
    bios = NetBIOS()
    srv_name = bios.queryIPForName(remote_smb_ip, timeout=timeout)
  except:
    print('getBIOSName: timeout too short?')
  finally:
    bios.close()
    # print('bios name = ' + srv_name[0])
    return srv_name[0]


def getRemoteDir(username, password, my_name, remote_name, remote_ip, path, service_name):
  print('getRemoteDir() starts...')
  conn = connect(username, password, my_name, remote_name, remote_ip)
  if conn:
    try:
      files = conn.listPath(service_name, path)

      for file in files:
          print(file.filename)

    except Exception as e:
      print(e)
    finally:
      conn.close()

  else:
    print('connect() failed!')
  return None


def createRemoteDir(username, password, my_name, remote_name, remote_ip, path, service_name):
  conn = connect(username, password, my_name, remote_name, remote_ip)
  if conn:
    try:
      conn.createDirectory(service_name, path)
    except Exception as e:
      fmt = 'conn.listPath({}, {}, {}) threw {}: {}'
      print(fmt.format(service_name, path, pattern, type(e), e))
    finally:
      conn.close()
  else:
    print('connect() failed!')
  return None

def removeRemoteDir(username, password, my_name, remote_name, remote_ip, path, service_name):
  conn = connect(username, password, my_name, remote_name, remote_ip)
  if conn:
    try:
      conn.deleteDirectory(service_name, path)
    except Exception as e:
      print(e)
    finally:
      conn.close()
  else:
    print('connect() failed!')
  return None

def renameRemoteDir(username, password, my_name, remote_name, remote_ip, old_path, new_path, service_name):
  conn = connect(username, password, my_name, remote_name, remote_ip)
  if conn:
    try:
      conn.rename(service_name, old_path, new_path)
    except Exception as e:
      print(e)
    finally:
      conn.close()
  else:
    print('connect() failed!')
  return None

def connect(username, password, my_name, remote_name, remote_ip):
  smb_structs.SUPPORT_SMB2 = True
  conn = SMBConnection(username, password, my_name, remote_name, use_ntlm_v2 = True)
  try:
    conn.connect(remote_ip, 139) #139=NetBIOS / 445=TCP
  except:
    print("cannot connect")
  return conn

def getServiceName(username, password, my_name, remote_name, remote_ip):
  conn = connect(username, password, my_name, remote_name, remote_ip)
  if conn:
    shares = conn.listShares()
    for s in shares:
      if s.type == 0:  # 0 = DISK_TREE
        return s.name
    conn.close()
  else:
    return ''

def delete_remote_file(username, password, my_name, remote_name, remote_ip, path, filename, service_name):
  conn = connect(username, password, my_name, remote_name, remote_ip)
  if conn:
    try:
        conn.deleteFiles(service_name, path+filename)
    except Exception as e:
        print(e)
    finally:
        conn.close()
        return None

    print('Remotefile ' + path + filename + ' deleted')
    conn.close()

  else:
    print('connect() failed!')
  return None


def upload(username, password, my_name, remote_name, remote_ip, path, filename, service_name):
    conn = connect(username, password, my_name, remote_name, remote_ip)
    if conn:
        print('File %s' % (filename))
        print('\nstart upload...')

        with open(filename, 'rb') as file_obj:
          t = timer()
          filesize = conn.storeFile(service_name, path+filename, file_obj)
          elapsed = timer() - t

        filesize_kb = filesize / 1024.0
        filesize_mb = filesize / (1024.0 * 1024.0)

        print('Size = %.2f Mbytes' % (filesize_mb))
        print('Speed = %.2f KBytes/s = %.2f Mbytes/s' % (filesize_kb / elapsed, filesize_mb / elapsed))

        print('upload finished')
        conn.close()


def download(username, password, my_name, remote_name, remote_ip, path, filename, service_name):
    conn = connect(username, password, my_name, remote_name, remote_ip)
    if conn:
        attr = conn.getAttributes(service_name, path+filename)

        filesize_kb = attr.file_size / 1024.0
        filesize_mb = attr.file_size / (1024.0 * 1024.0)

        print('File %s = %.2f Mbytes' % (filename, filesize_mb))
        print('\nstart download...')

        tmpf = NTF()
        try:
            t = timer()
            conn.retrieveFile(service_name, path+filename, tmpf)
            elapsed = timer() - t
        except Exception as e:
            print(e)

        print('Speed = %.2f KBytes/s = %.2f Mbytes' % (filesize_kb / elapsed, filesize_mb / elapsed))

        shutil.copy(tmpf.name, filename)

        tmpf.close()

        os.chmod(filename, 0o666)

        print('download finished')

        conn.close()


if __name__ == '__main__':

    username = '1'
    password = '1'
    my_name = 'pc'
    remote_ip = '192.168.0.1'
    # remote_name = 'D-LINK'
    remote_name = getBIOSName('192.168.0.1')
    service_name = getServiceName(username, password, my_name, remote_name, remote_ip)
    filename = 'ny.jpg'
    path='/'

    # getRemoteDir(username, password, my_name, remote_name, remote_ip, path,  service_name)

    # createRemoteDir(username, password, my_name, remote_name, remote_ip, 'my_dir', service_name)

    # renameRemoteDir(username, password, my_name, remote_name, remote_ip, path + 'my_dir', path + 'his_dir', service_name)

    # removeRemoteDir(username, password, my_name, remote_name, remote_ip, 'zhora', service_name)


    # download(username, password, my_name, remote_name, remote_ip, path, filename, service_name)

    # upload(username, password, my_name, remote_name, remote_ip, path, filename, service_name)

    # delete_remote_file(username, password, my_name, remote_name, remote_ip, path, filename, service_name)
