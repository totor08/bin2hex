## Convert binary file into Intel HEX format file.

usage: bin2hex [-h] [-l [LOADADDRESS]] [-s [STARTADDRESS]] [-w WIDTH] filename

Convert a binary file into Intel HEX format

positional arguments:
  filename              binary filename

optional arguments:
  -h, --help            show this help message and exit
  -l [LOADADDRESS], --loadAddress [LOADADDRESS]
                        Load Address in ABCD hex format
  -s [STARTADDRESS], --startAddress [STARTADDRESS]
                        Start Address in ABCD hex format
  -w WIDTH, --width WIDTH
                        Bytes per line

--s set the tail record launch address ( refer to Intel HEX format ), 0000 by default
--l set the address where the binary file is supposed to be loaded, 0000 by default
--w set the decimal byte count per line, 16 by default.

example :
bin2hex.py t1.bin -l 1234 -s 5678 -w 6
:061234003132333435367F
:06123A0037383930313273
:041240003334350A04
:0056780131

bin2hex t1.bin
:100000003132333435363738393031323334350ADA
:00000001FF

