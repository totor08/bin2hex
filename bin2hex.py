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
# open the file in read binary mode
f = open(filename,"rb")
while size > 0 :
    # if remaining bytes count is less than the width
    #  set the width
    if width > size :
        width = size
    # decrement remaining count size by width
    size -= width
    # read the file by width bytes
    buf=f.read(width)
    # set a list with width, address in big indian format,
    #  and the 0 marker
    bl=[width, int(load/256) & 255, load & 255, 0]
    # increment the address by width
    load += width
    # append the list with the bytes just read
    for i in range(0,width) :
        bl.append(buf[i])
    # initialize the checksum
    chk=0
    # print the leading ":" with no carriage return
    print(":",end="")
    # for each element of the list
    for i in bl :
        # compute the checksum
        chk += i
        # print the byte in 2 hexadecimal format, with no carriage return
        print("{:02X}".format(i), end="")
    # keep the right byte of the checksum
    chk = (-chk) & 255
    # print the checksum in a 2 hexadecimal format, with a line feed
    print("{:02X}".format(chk))

# print the start address record the same way
bl=[0,int(start/256)&255, start & 255, 1 ]
print(":",end="")
chk=0
for i in bl :
    chk += i
    print("{:02X}".format(i), end="")
chk = (-chk) & 255
print("{:02X}".format(chk))

# close the input file
f.close
