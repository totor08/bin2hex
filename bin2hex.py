#!/usr/bin/python3

import sys
import os
import argparse

parser = argparse.ArgumentParser(
        prog='bin2hex',
        description='Convert a binary file into Intel HEX format')
parser.add_argument("filename",help="binary filename")
parser.add_argument("-l","--loadAddress",help="Load Address in ABCD hex format", nargs='?', default="0")
parser.add_argument("-s","--startAddress", help="Start Address in ABCD hex format", nargs='?', default="0")
parser.add_argument("-w","--width", help="Bytes per line", default=16, type=int)
args = parser.parse_args()

# get filename
filename = args.filename

# get file size
size = os.stat(filename).st_size

# get width command line option
width = args.width

# get load address
start = int(args.startAddress,16)

# get start address
load = int(args.loadAddress,16)

f = open(filename,"rb")
while size > 0 :
    if width > size :
        width = size
    size -= width
    buf=f.read(width)
    bl=[width, int(load/256) & 255, load & 255, 0]
    load += width
    for i in range(0,width) :
        bl.append(buf[i])
    chk=0
    print(":",end="")
    for i in bl :
        chk += i
        print("{:02X}".format(i), end="")
    chk = (-chk) & 255
    print("{:02X}".format(chk))

bl=[0,int(start/256)&255, start & 255, 1 ]
print(":",end="")
chk=0
for i in bl :
    chk += i
    print("{:02X}".format(i), end="")
chk = (-chk) & 255
print("{:02X}".format(chk))

f.close
