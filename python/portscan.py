#!/usr/bin/env python

import socket
import argparse
import sys
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('host')
args = parser.parse_args()

t1 = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((args.host, port))
        if result == 0:
            print("Port: {} open".format(port))
        sock.close()
except KeyboardInterrupt:
    sys.exit()

t2 = datetime.now()
print("Scanning completed in: {}".format(t2-t1))
