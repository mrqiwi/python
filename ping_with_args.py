#!/usr/bin/python3

import subprocess
import argparse


def ping_ip(ip_address, count):

    reply = subprocess.run('ping -c {count} -n {ip}'
                           .format(count=count, ip=ip_address),
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stdout+reply.stderr

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Ping script')
	parser.add_argument('host', action="store", help="IP or name to ping")
	# parser.add_argument('-a', action="store", dest="ip", required=True)
	parser.add_argument('-c', action="store", dest="count", default=2, type=int)
	args = parser.parse_args()

	rc, message = ping_ip(args.host, args.count)

	print(message)
