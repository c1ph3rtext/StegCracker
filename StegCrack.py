#!/usr/bin/python
#Python Script

import os, sys

try:
    file = sys.argv[1]
    list = sys.argv[2]
    print (f"\nCracking {file}.....")
    hack = (f''' \n for i in $(cat {list}); do steghide --extract -sf {file} -p $i 2>/dev/null && echo -e "\nPassword: $i" && break; done''')
    os.system(hack)

except IndexError as o:
   print ("Usage: python StegCrack.py file_to_crack passwd_file")
   sys.exit()

except KeyboardInterrupt as k:
   print ('\nStopped!')
   sys.exit()

