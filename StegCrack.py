#!/usr/bin/python
#Python Script

import os, sys

file = sys.argv[1]
list = sys.argv[2]

print (f"\nCracking {file}.....")

try:
    hack = (f''' \n for i in $(cat {list}); do steghide --extract -sf {file} -p $i 2>/dev/null && echo -e "\nPassword: $i" && break; done''')
    os.system(hack)
except KeyboardInterrupt as k:
   print ('\nStopped!')
   sys.exit()

