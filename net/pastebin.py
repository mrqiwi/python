#!/usr/sbin/python3
import os
import sys
import requests

def create_request(filename):
    filetype = os.path.splitext(filename)[1][1:]
    code = open(filename, 'r').read()

    data = {}
    data['api_dev_key'] = os.getenv('PASTEBIN')
    data['api_option'] = 'paste'
    data['api_paste_code'] = code
    data['api_paste_format'] = filetype
    data['api_paste_private'] = '0'
    data['api_paste_expire_date'] = '10M'

    return data

def send_request(data):
    url = 'https://pastebin.com/api/api_post.php'
    req = requests.post(url, data=data)
    return req.text

if __name__ == "__main__":

    if (len(sys.argv) != 2):
        print("usage: script <filename>");
        sys.exit(1)

    data = create_request(sys.argv[1])
    result = send_request(data)

    print(result)


