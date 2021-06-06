import sys
from os import system
from time import sleep
system("title "+ '_NFO_')
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=90))
arguments = sys.argv
filename = arguments[-1]
# sys.stdout.reconfigure(encoding='dos')

# cp437 works great

if len(arguments) != 2:
    print('Please specify which file to open or make this program the default program')
    print('to open NFO files or other kind of text files')
    sleep(5)
    exit()

with open(filename, 'r', encoding='cp437') as f:
    for line in f:
        # print(line, end='')
        sys.stdout.write(line)

i = input()