## Convert binary file into Intel HEX format file.

usage: bin2hex [-h] [-l [launchAddr]] [-s [locationAddr]] [-w WIDTH]
               filename

Convert a binary file into Intel HEX format

positional arguments:
  filename              binary filename

optional arguments:
  -h, --help            show this help message and exit
  -l [LAUNCHADDRESS], --launchAddress [LAUNCHADDRESS]
                        Launch Address in ABCD hex format
  -s [STARTADDRESS], --startAddress [STARTADDRESS]
                        Mapping Address in ABCD hex format
  -w WIDTH, --width WIDTH
                        Bytes per line

--launchAddress option set the tail record launch address ( refer to Intel HEX format )
--startAddrees option set the address where the binary file is supposed to be loaded.
--width option set the byte count per line, 16 by default.
