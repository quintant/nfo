import sys
from os import system
from time import sleep
from random import choice

system("title " + "NFO")
# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=50, cols=90))
arguments = sys.argv
filename = arguments[-1]
# sys.stdout.reconfigure(encoding='dos')

colors = [
    "\u001b[31m",
    "\u001b[32m",
    "\u001b[33m",
    "\u001b[34m",
    "\u001b[35m",
    "\u001b[36m",
]
color = choice(colors)

if len(arguments) != 2:
    print("Please specify which file to open or make this program the default program")
    print("to open NFO files or other kind of text files")
    sleep(5)
    exit()

with open(filename, "r", encoding="cp437") as f:
    for line in f:
        for ch in line:
            if ch.isascii():
                print(ch, end="")
            else:
                print(f"{color}{ch}\u001b[0m", end="")


i = input()
